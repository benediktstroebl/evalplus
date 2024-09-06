def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    db_suffix = "db"
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]
    
    # Add db prefixes and suffixes
    binary = db_prefix + binary + db_suffix
    
    return binary