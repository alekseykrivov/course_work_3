import requests
from datetime import datetime

def load_data(path):
    try:
        response = requests.get(path)
        if response.status_code == 200:
            return response.json(), "INFO: Data received"
        return None, f"WARNING: Incorrect answer. Status {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: Connection error"


def get_filtred_data(data, filtred_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtred_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]

def get_formatted_data(data):
    formatted_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]

        if "from" in i:
            sender = i["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = "", "[MASKED]"

        recipient = f"**{i['to'][-4:]}"
        amount = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\
{date} {description} {sender_info} {sender_bill} -> Счет {recipient}
{amount}
""")
    return formatted_data


