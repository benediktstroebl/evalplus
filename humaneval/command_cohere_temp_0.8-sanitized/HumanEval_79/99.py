def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = '{:b}'.format(decimal)
    return 'db' + bin_str + 'db'
decimal = 15