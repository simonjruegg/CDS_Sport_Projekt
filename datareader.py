from config import DATA_DIR

## Load data from the specified data directory
def load_data(filename):
    filepath = DATA_DIR + filename
    with open(filepath, 'r') as file:
        data = file.read()
    return data