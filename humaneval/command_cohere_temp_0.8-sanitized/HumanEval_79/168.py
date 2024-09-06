def decimal_to_binary(decimal):
    binary_string = "{0:b}".format(decimal)
    return "db{0}db".format(binary_string)
decimal = 15