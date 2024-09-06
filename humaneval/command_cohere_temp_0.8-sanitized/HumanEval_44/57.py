def change_base(x, base):
    if base < 10:
        return str(x).zfill(math.ceil(math.log(x, base)))
    return x.convert(base)