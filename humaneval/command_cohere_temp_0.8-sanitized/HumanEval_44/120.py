def change_base(x, base):
    return str(x) in ['0', '1'] and str(x) * base or list(str(x))[:-1] * base