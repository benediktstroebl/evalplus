def decimal_to_binary(decimal):
    binary = bin(decimal).replace('0b', 'db').rjust(64, '0')
    return binary + 'db'