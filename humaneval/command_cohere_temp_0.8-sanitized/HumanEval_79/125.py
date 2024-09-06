def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = "{0:b}".format(decimal)    # Convert decimal to binary and format result
    return "db{0}db".format(bin_str)     # Add extra characters 'db' at the beginning and end
decimal = 15