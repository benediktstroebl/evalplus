def change_base(x, base):
    return bin(x)[2:].rjust(calc_len(x), '0')[::-1] if base == 2 else adjust_to_base(x, base)
def adjust_to_base(x, base):
    # convert to decimal first if base is not 2
    tmp_decimal = str(int(x))
    if base != 10:
        tmp_decimal = change_base(tmp_decimal, 10)
    return multiply(tmp_decimal, base)
def multiply(num1, num2):
    return str(int(num1) * int(num2))
def calc_len(x):
    # calculate length of binary string with decimal value x
    return len(bin(int(x))[2:])