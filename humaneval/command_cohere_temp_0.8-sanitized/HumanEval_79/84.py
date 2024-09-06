def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    binary_string = bin(decimal)[2:]
    db_suffix = "db"
    return db_prefix + binary_string + db_suffix
decimal = 15