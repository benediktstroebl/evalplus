def decimal_to_binary(decimal):
    bin_str = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return f"db{bin_str}db"