def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # strip '0b' from binary representation
    return 'db' + bin_str + 'db'