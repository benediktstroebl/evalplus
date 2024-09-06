def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens = int(n) / 10
        if tens == 0:
            return str(n)
        roman_n = []
        for i in range(2, tens + 1):
            roman_n.extend([str(i) for i in range(1, 5)][::-1])
        roman_n.extend([str(n)[:-1] for n in range(10, tens + 1) if n != 10])
        return ''.join(roman_n)