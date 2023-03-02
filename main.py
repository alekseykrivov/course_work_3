import utils
from utils import load_data, get_filtred_data, get_last_data, get_formatted_data



def main():
    JSON_DATA_URL = "https://www.jsonkeeper.com/b/H7GP"
    COUNT_LAST_VALUES = 5
    FILTRED_EMPTY_FROM = True

    data, info = load_data(JSON_DATA_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")
    data = get_filtred_data(data, FILTRED_EMPTY_FROM)
    data = get_last_data(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
