def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for _ in range(thousands):
            roman_thousands += "m"
        if rest == 0:
            return roman_thousands + "i"
        roman_numerals = [
            ("i", "ii", "iii", "iv", "v"),
            ("vi", "vii", "viii", "ix"),
            ("x", "l", "lx", "lxi", "lxii", "lxiii", "lxiv", "xv"),
            ("xvi", "xvii", "xviii", "xix"),
            ("xx", "lxx", "lxxi", "lxxii", "lxxiii", "lxxiv", "lxxv"),
            ("xxvi", "xxvii", "xxviii", "xxix"),
            ("xxx", "lxxx", "lxxxi", "lxxxii", "lxxxiii", "lxxxiv", "lxxxv"),
            ("xxxx", "xxxxi", "xxxxii", "xxxxiii", "xxxxiv", "xxxxv")
        ]
        roman = roman_numerals[rest // 5]
        return roman_thousands + "".join(roman[i] for i in range(rest // 5))