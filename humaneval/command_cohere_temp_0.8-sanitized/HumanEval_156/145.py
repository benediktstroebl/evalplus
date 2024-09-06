def int_to_mini_roman(num):
    if num < 1000:
        roman_numbers = {
            1: 'i',
            4: 'iv',
            5: 'v',
            9: 'ix',
            10: 'x',
            40: 'l',
            50: 'l',
            90: 'xc',
            100: 'c',
            400: 'cd',
            500: 'd',
            900: 'cm',
            1000: 'm'
        }
        result = []
        for count in range(1, 1001):
            if num >= count:
                result.append(roman_numbers[count])
                num -= count
        result = ''.join(reversed(result))
        return result.lower()
    else:
        return "Error!"