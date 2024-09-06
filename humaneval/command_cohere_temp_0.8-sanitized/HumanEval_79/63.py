def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = f"db{bin(decimal)[2:]}.join(['01']*int(x))[2:-1]"
    return f"db{bin_str}db"
decimal = 15