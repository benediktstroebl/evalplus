def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', 'db').rjust(len(str(decimal)), '0')"
    return binary