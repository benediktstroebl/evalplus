def int_to_mini_roman(num):
    converter = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }
    result = []
    for i in range(1, 1001):
        if num >= i:
            num_left = num // i
            result.append(converter[i])
            result.append(converter[num_left])
            num %= i
    return ''.join(result)[::-1]