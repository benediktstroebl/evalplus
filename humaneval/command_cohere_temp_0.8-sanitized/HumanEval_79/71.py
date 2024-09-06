def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]
    
    # Ensure leading zeros
    padded_binary = '0' * (len(db_prefix) - len(binary)) + binary + '0' * (len(db_suffix) - len(binary))
    
    return db_prefix + padded_binary + db_suffix
decimal = 15