def decimal_to_binary(decimal):
    """Convert a decimal number to binary format with extra 'db' characters."""
    binary = f"db{bin(decimal)[2:]}.strip('b') + 'db'"
    return binary