def decimal_to_binary(decimal):
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal), '0') + 2)
    return binary