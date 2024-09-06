def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return f"db{binary}db"