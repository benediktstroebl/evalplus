def int_to_mini_roman(num):
    mini_roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    tens = ['x', 'l', 'c', 'd', 'm']
    hundreds = ['c', 'cc', 'cd', 'd', 'dc', 'cm']

    result = []
    while num > 0:
        remainder = num % 10
        if remainder == 0:
            result.extend(hundreds[(num // 100) - 1])
            break
        else:
            result.extend(mini_roman[remnant - 1])
            result.append(tens[num // 10 % 10])
            num //= 10

    return ''.join(result).lower()