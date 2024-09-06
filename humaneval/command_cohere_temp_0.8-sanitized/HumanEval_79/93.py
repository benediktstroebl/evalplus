def decimal_to_binary(decimal):
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)