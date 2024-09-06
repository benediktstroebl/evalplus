def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))