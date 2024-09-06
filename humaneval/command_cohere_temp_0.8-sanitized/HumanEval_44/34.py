def change_base(x, base):
    return str(x)
    if base != 10:
        return bin(x)[2:].decode("utf-8").translate(str.maketrans('01','10'))
    else:
        return str(x)