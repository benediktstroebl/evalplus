def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return 'db' + bin_str + 'db'    # Add 'db' at the beginning and end for formatting