def int_to_mini_roman(n):
    if n < 1:
        return ""

    symbols = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
    tens = ["","xx","xxx","xxxx","xv","xix","xxi","xxii","xxiii","xxiv","xxv"]
    hundreds = ["","c","cc","ccc","cd","cdr","cdrr","cdrrr","cdd","cddr","cddrr","cddrrr"] \
              ["","ccc","cccd","cccdr","cccdrr","cccdrrr","ccee","cceer","cceerr","cceerrr"]

    roman = []
    while n > 0:
        reminder = n % 1000
        if reminder >= 100:
            roman.append(hundreds[reminder // 100])
            roman.append(tens[reminder % 100 // 10])
            roman.append(symbols[reminder % 10])
        elif reminder >= 50:
            roman.append(tens[reminder // 50])
            roman.append(symbols[reminder % 10])
        elif reminder >= 10:
            roman.append(symbols[reminder // 10])
            roman.append(symbols[reminder % 10])
        else:
            roman.append(symbols[reminder])

        n //= 1000

    return "".join(roman)