def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for i in range(1, thousands + 1):
            roman_thousands += "m"
        roman_rest = int_to_mini_roman(rest)
        return f"{roman_thousands}{roman_rest}"