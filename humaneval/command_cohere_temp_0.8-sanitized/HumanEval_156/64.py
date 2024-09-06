def int_to_mini_roman(num):
    if num < 1000:    
        conversions = [
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

        result = ''
        for i in range(len(conversions)):
            while num >= conversions[i][0]:
                num -= conversions[i][0]
                result += conversions[i][1]
        return result.lower()
    else:
        return 'Error: Int exceeds maximum allowed!'