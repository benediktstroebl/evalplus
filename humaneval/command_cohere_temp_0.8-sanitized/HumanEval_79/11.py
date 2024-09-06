def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation, with extra '0's and '1's for correct formatting."""
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return binary + 'db'