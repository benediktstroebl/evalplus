def decimal_to_binary(decimal):
    """Returns a string representing the binary equivalent of the decimal number, with extra '0's and '1's for formatting."""
    bin_str = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return f"db{bin_str}db"