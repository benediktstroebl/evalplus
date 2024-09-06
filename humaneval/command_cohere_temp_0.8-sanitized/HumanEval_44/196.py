def change_base(x, base):
    return bin(x)[2:].rjust(calc_len(x), '0')[::-1] if base == 2 else adjusting_digit(x, base)
def adjusting_digit(x, base):
    result = []
    while x > 0:
        x, r = divmod(x, base)
        result.append(str(r))
    return "".join(reversed(result))
def calc_len(x):
    base = 2
    while x > base:
        x //= base
        base //= 2
    return max(len(bin(x)[2:]), len(adjusting_digit(x, base)))