def change_base(x, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    return str(int(x) << int(math.log(base, 2))).translate(str.maketrans('', '', digits[1:]))