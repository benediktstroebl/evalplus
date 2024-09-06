def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        rom_thousands = chr(ord("m") + thousands)
        rom_rest = int_to_mini_roman(rest)
        return f"{rom_thousands}{rom_rest}"