import pandas as pd

gender_train = pd.read_csv("data/gender_train.csv")
print(gender_train.head())
transactions = pd.read_csv("data/transactions.csv", nrows=1000000)
print(transactions.head())

# считается плохо, нужно править, посмотрите на вывод head и на содержимое gender_train.csv, tr_types.csv
# tr_types = pd.read_csv("data/tr_types.csv")
# print(tr_types.head())

# считается с ошибкой, тоже нужно править
# tr_mcc_codes = pd.read_csv("data/tr_mcc_codes.csv")
# print(tr_mcc_codes.head())
