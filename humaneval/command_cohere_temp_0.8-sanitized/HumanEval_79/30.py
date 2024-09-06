def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    binary_string = bin(decimal)[2:]
    binary_string = binary_string.zfill(len(bin(decimal)[2:]) + 2*len(db_prefix) + len(db_suffix))
    
    return db_prefix + binary_string + db_suffix
decimal = 15