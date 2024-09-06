def int_to_mini_roman(num):
    if num < 1000:   
        conversion_dict = [
            (1000, 'm'), 
            (900, 'cm'),
            (500, 'd'), 
            (400, 'cd'),
            (100, 'c'), 
            (90, 'xc'),
            (50, 'l'), 
            (40, 'xl'),
            (10, 'x'), 
            (9, 'ix'),
            (5, 'v'), 
            (4, 'iv'),
            (1, 'i')
        ]

        result = []
        for value, char in conversion_dict:
            count = num // value
            result.extend([char] * count)
            num %= value

        return ''.join(result).lower()
    else:
        return "Error!"