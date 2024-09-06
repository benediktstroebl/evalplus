def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', '').rjust(len(str(decimal)), '0')"
    return f"db{binary}db"
decimal = 15