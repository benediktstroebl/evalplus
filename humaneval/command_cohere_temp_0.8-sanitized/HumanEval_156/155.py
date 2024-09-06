def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_letters = ['m','m','d','d','c','c','i','i','x','x','l','l','v','v','i']
    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            num -= roman_values[i]
            result.append(roman_letters[i])
    return ''.join(result)