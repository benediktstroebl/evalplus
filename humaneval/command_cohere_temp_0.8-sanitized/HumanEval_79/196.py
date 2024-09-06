def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Remove '0b' from binary representation
    return 'db' + binary + 'db'