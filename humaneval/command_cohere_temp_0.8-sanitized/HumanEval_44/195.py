def change_base(x, base):
    return str(x)
    if base != 10:
        return int(x, 10) // int(x, base) * base