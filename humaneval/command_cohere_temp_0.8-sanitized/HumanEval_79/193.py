def decimal_to_binary(decimal):
    """Returns binary representation of decimal number with extra zeros and ones added at the beginning and end"""
    binary_string = bin(decimal)[2:]
    return "db" + binary_string + "db"