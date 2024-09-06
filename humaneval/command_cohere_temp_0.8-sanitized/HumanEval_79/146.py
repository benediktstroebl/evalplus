def decimal_to_binary(decimal):
    """Convert a decimal number to binary representation."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary