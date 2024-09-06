def change_base(x, base):
    return str(x).encode([(len(str(x))-1)] * x, base)