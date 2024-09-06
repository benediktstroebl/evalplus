def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation, with extra '0's and '1's for proper formatting."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary