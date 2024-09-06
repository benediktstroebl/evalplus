def decimal_to_binary(decimal):
    """Convert a decimal number to binary format string."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    binary_str = '{0:b}'.format(decimal) # convert decimal to binary string
    return db_prefix + binary_str + db_suffix # prepend and append with 'db'
decimal = 15