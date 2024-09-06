def decimal_to_binary(decimal):
    """
    Convert a decimal number to binary format.
    """
    binary = bin(decimal).replace('0b', 'db').replace('{}', 'db')
    return binary