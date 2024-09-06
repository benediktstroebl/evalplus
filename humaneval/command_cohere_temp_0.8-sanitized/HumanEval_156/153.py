def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    roman = {}
    current = ''

    for i in range(1, 1000):
        num = i
        roman_num = []

        while num > 0:
            remainder = num % 5
            if roman.get(remainder):
                roman_num.extend(roman[remainder])
                num //= 5
            else:
                roman[remainder] = [str(remainder)]
                num //= 5

        if roman_num:
            current = roman_num[0] + current

        if i == n:
            break

    return current.lower()