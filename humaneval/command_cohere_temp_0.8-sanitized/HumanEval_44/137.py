def change_base(x, base):
    return str(x).encode([(len(str(x)), base)])