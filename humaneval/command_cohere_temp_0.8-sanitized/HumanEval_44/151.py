def change_base(x, base):
    return bin(x)[2:].zfill(len(bin(x)[2:]) * int(base))