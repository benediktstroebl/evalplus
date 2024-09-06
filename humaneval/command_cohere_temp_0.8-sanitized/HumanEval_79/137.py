def decimal_to_binary(decimal):
    if not isinstance(decimal, int):
        raise ValueError("An integer is expected")
    
    binary = bin(decimal)[2:]
    return f"db{binary}db"