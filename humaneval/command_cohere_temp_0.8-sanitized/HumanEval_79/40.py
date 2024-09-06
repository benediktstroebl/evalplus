def decimal_to_binary(decimal):
    """Convert a decimal number to binary format string."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]

    # Add leading zeros if needed
    zfill = len(db_prefix) - len(binary)
    binary = ('0' * zfill) + binary
    
    # Append db prefixes and suffixes
    binary = db_prefix + binary + db_suffix
    
    return binary
decimal = 15