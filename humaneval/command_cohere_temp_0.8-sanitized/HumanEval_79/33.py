def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = f"db{bin(decimal)[2:]}.join(['0','1'])[2:-1]"
    return binary