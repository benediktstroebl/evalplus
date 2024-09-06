def decimal_to_binary(decimal):
    bin_string = bin(decimal)[2:]
    return 'db' + bin_string + 'db'