def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens, rest = divmod(n, 10)
        if tens == 1:
            return f"i{int_to_mini_roman(rest)}"
        elif tens > 1:
            return f"{tens}x{int_to_mini_roman(rest)}"
        else:
            return f"{int_to_mini_roman(tens)}{int_to_mini_roman(rest)}"