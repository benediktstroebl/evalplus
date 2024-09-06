def decimal_to_binary(decimal):
    """Convert a decimal number to binary format
    
    Extra characters 'db' are added at the beginning and end of the string for formatting."""
    binary_str = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary_str + "db"
decimal = 15