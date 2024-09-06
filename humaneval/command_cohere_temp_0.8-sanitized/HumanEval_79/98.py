def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    binary_str = '{:b}'.format(decimal)
    return f"{db_prefix}{binary_str}{db_suffix}"
decimal = 15