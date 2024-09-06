def change_base(x, base):
    return bin(x)[2:].zfill(ceil(log2(x)) * (base <= 10)) if base != 10 else str(x)