def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = "{0:b}".format(decimal)    # Convert decimal to binary and prefix with '0b'
    return "db"+bin_str+"db"              # Add 'db' characters at the beginning and end