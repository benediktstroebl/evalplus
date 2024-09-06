def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # Removing '0b' from binary string
    return 'db' + bin_str + 'db'