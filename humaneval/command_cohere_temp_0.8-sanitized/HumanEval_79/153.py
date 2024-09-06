def decimal_to_binary(decimal):
    """Convert a decimal number to binary format string."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary