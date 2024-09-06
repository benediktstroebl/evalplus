def decimal_to_binary(decimal):
    binary_str = '{0:b}'.format(decimal)
    return 'db' + binary_str + 'db'