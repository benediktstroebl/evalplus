def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b'
    return 'db' + binary + 'db'  # Add 'db' characters at the beginning and end