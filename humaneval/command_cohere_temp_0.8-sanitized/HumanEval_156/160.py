def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        rom_thousands = ""
        for _ in range(thousands):
            rom_thousands += "m"
        rom_rest = []
        while rest:
            remainder = rest % 5
            if remainder == 0:
                rom_rest.append("0")
            elif remainder == 1:
                rom_rest.append("i")
            elif remainder == 2:
                rom_rest.append("ii")
            elif remainder == 3:
                rom_rest.append("iii")
            elif remainder == 4:
                rom_rest.append("iv")
            rest //= 5
        return f"{rom_thousands} {(''.join(rom_rest))}"