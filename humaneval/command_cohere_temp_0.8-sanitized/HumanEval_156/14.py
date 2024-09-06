def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_mapping = [
            ('i', 'i'),
            ('iv', 'iv'),
            ('v', 'v'),
            ('ix', 'ix'),
            ('x', 'x'),
            ('lx', 'lx'),
            ('l', 'l'),
            ('xc', 'xc'),
            ('c', 'c'),
            ('cd', 'cd'),
            ('d', 'd'),
            ('cm', 'cm'),
            ('m', 'm'),
        ]

        roman_num = []
        for map_ in roman_mapping:
            while n >= map_[1]:
                n -= map_[1]
                roman_num.append(map_[0])

        return ''.join(roman_num).lower()
    else:
        return "Invalid Input!"