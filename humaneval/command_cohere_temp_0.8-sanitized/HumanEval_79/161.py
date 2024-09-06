def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation, with extra '0's and '1's for correctness"""
    bin_str = "{0:b}".format(decimal)
    return "db"+bin_str+"db"