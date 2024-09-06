def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens, rest = divmod(n, 10)
        if tens == 1:
            return f"{rest}x"
        elif tens > 1:
            return f"{tens}x{int_to_mini_roman(rest)}"
        else:
            return f"{rest}{int_to_mini_roman(tens)}"