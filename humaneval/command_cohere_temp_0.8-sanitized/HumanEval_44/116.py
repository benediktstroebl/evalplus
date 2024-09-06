def change_base(x, base):
    return bin(x)[2:].rjust(ceil(log2(x)), '0') if base == 2 else f'{x:b}{len(str(x)) - 2 * len(str(x).rstrip("0"))}:b'