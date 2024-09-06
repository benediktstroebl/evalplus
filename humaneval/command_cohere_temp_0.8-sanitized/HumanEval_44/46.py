def change_base(x, base):
    return bin(x)[2:].rjust(calc_len(x), '0')[::-1] if base == 2 else adjust_to_base(x, base)
def adjust_to_base(x, base):
    digits = '0123456789ABCDEF'
    ret = []
    while x > 0:
        x, r = divmod(x, base)
        ret.append(digits[r])
    return ''.join(ret)[::-1]
def calc_len(x):
    base = 2
    while x > 1:
        x //= base
        base //= 2
    return len(bin(base)[2:])