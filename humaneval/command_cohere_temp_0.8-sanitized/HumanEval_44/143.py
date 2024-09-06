def change_base(x, base):
    return bin(x)[2:].zfill(len(str(x)) * (len(bin(base)) - 2)) if base < 2 else hex(x).rstrip('0').rstrip('L').zfill(len(str(x)) + 2)