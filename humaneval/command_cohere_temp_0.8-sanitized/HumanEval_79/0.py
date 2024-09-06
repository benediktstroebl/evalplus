def decimal_to_binary(decimal):
    """Returns binary string for given decimal number with extra 'db' chars"""
    bin_str = f"db{bin(decimal)[2:]}.replace('0b', '').rjust(len(str(decimal)), '1')"
    return f"db{bin_str}db"