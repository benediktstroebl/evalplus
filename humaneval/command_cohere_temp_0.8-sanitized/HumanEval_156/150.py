def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, hundreds, tens, remainder = divmod(n, 1000)
        if thousands:
            return ""
        rom_hundreds = []
        for x in range(hundreds):
            rom_hundreds.append("c")
        rom_ten = ""
        if tens:
            for x in range(tens):
                rom_ten += "x"
        rom_rem = []
        for x in range(remainder):
            rom_rem.append("i")
        roman = rom_hundreds + rom_ten + rom_rem
        roman = "".join(roman).lower()
        return roman