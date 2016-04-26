import os


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
    return []

def query_data(data):
    pass

if __name__ == '__main__':
    main()
