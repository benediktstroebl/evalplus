def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
        result = []
        for i in range(len(roman_values)):
            while n >= roman_values[i]:
                result.append(roman_numerals[i])
                n -= roman_values[i]
        return ''.join(result)
    else:
        return "Invalid Input!"