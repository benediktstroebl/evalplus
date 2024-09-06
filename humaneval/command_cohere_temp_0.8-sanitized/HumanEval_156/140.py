def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        if thousands:
            return str(thousands) + "m" + int_to_mini_roman(rest)
        digits, num = divmod(rest, 5)
        if digits:
            return "i" * digits + num
        else:
            return str(num)