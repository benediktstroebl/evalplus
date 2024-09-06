def decimal_to_binary(decimal):
    """Convert a decimal number to binary format"""
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)
decimal = 15