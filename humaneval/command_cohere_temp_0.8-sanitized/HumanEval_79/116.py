def decimal_to_binary(decimal):
    """Returns binary string for given decimal number with 'db' borders"""
    bin_num = bin(decimal)[2:]
    return f"db{bin_num}db"