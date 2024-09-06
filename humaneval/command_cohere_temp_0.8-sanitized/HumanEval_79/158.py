def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    binary = '{0:b}'.format(decimal)
    return 'db' + binary + 'db'
decimal = 15