def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens = int(n) / 10
        if tens == 0:
            return str(n)
        roman_digits = [
            "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"
        ]
        roman_tens = [
            "x", "l", "c", "d", "m"
        ]
        return (roman_tens[tens] + roman_digits[n % 10] +
                (str(tens))[1:])