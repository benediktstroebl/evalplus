def int_to_mini_roman(n):
    if n < 1000:
        result = []
        for x in range(0, n + 1):
            if x != 0:
                result.append(str(roman_num[x]))
        result.reverse()
        return ''.join(result)
    else:
        return 'Error: Restrictions are 1 <= num <= 1000'
roman_num = {
    1: 'i',
    4: 'iv',
    5: 'v',
    9: 'ix',
    10: 'x',
    40: 'lxx',
    50: 'l',
    90: 'xc',
    100: 'c',
    400: 'cd',
    500: 'd',
    900: 'cm',
    1000: 'm'
}