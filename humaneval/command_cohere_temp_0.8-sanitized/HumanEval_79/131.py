def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    db_suffix = "db"
    binary_string = "{0:b}".format(decimal)
    return db_prefix + binary_string + db_suffix