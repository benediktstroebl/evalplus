def decimal_to_binary(decimal):
    binary_str = '{:b}'.format(decimal)
    return 'db' + binary_str + 'db'