def decimal_to_binary(decimal):
    binary_str = f"db{bin(decimal)[2:]}.replace('0b', 'db')[2:-1]"
    return binary_str