def change_base(x, base):
    return bin(x)[2:].zfill(ceil(log2(x)) * len(str(base))).translate(str.maketrans('01', str(base), str(base)[1:]))