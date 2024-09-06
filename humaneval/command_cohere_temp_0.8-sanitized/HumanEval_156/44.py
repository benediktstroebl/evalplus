def int_to_mini_roman(n):
    if n < 1:
        return ""

    symbols = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
    tens = ["", "x", "l", "c", "d", "m"]
    hundreds = ["", "c", "cc", "cd", "cm"]

    roman_num = []

    # Handle 1s
    while n >= 1:
        if n % 5 == 0:
            roman_num.append(symbols[4])
            n //= 5
        elif n % 10 == 0:
            roman_num.append(symbols[n // 10 - 1])
            n //= 10
        else:
            roman_num.append(symbols[n % 10 - 1])
            n //= 10

    # Handle 10s
    while n >= 10:
        roman_num.append(tens[n % 10 - 1])
        n //= 10

    # Handle 100s
    while n >= 100:
        roman_num.append(hundreds[n % 100 - 1])
        n //= 100

    return "".join(roman_num)