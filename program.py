import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    file_name = get_data_file()
    data = load_file(file_name)
    query_data(data)


def print_header():
    print('----------------------------------------')
    print('      REAL ESTATE DATA MINING APP       ')
    print('----------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        reader = csv.DictReader(fin, delimiter=',')
        purchases = []
        for row in reader:
            #print(row)
            #print("Bed count: {}".format(row['beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases


def load_file_basic(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        header = fin.readline().strip()
        print("found header: " + header)
        lines = []

        for line in fin:
            line_data = line.strip().split(',')
            bed_count = line_data[4]
            lines.append(line_data)
        print(lines[:5])


# def get_price(p):
#    return p.price

def query_data(data):  # list[Purchase]):

    # if data was sorted by price:
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)
    # most expensive house
    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))

    # least expensive house
    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))
    # average price house
    prices = []
    for pur in data:
        prices.append(pur.price)

    avg_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(avg_price)))

    # average price house of 2 bedroom houses
    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    avg_price = statistics.mean(prices)
    print("The average of a 2-bedroom home price is ${:,}".format(int(avg_price)))


if __name__ == '__main__':
    main()
