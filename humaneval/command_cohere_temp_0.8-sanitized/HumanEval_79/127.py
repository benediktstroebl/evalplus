def decimal_to_binary(decimal):
    bin_str = bin(decimal).replace('0b', 'db').rjust(len(str(decimal), '0') + 2)
    return bin_str