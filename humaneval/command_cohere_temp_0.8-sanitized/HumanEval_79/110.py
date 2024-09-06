def decimal_to_binary(decimal):
    binary_string = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return f"db{binary_string}db"