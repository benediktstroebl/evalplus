def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    roman = []
    while n > 0:
        number = n
        roman_num = []
        while number >= 10:
            roman_num.append(str(number % 10))
            number //= 10
        roman_num.reverse()
        roman.extend(roman_num)
        n -= sum(roman_num)
    return ''.join(map(str, roman))