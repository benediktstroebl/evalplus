def decimal_to_binary(decimal):
    return f"db{bin(decimal)[2:]}.replace('0b', 'db').rstrip('db')"