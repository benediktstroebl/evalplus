def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_digits = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            result.append(roman_digits[i])
            num -= roman_values[i]
    return ''.join(result)