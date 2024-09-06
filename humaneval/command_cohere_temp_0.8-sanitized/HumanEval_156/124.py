def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_mapping = [
            ('i', 'i'),
            ('iv', 'iv'),
            ('v', 'v'),
            ('ix', 'ix'),
            ('xl', 'xl'),
            ('xc', 'xc'),
            ('ixl', 'ixl'),
            ('ixc', 'ixc'),
            ('vxl', 'vxl'),
            ('vxj', 'vxj'),
            ('vxjr', 'vxjr'),
            ('vxjrtx', 'vxjrtx'),
            ('iix', 'iix'),
            ('ii', 'ii'),
            ('iii', 'iii'),
            ('iv', 'iv'),
            ('v', 'v'),
            ('ix', 'ix'),
            ('x', 'x'),
            ('xl', 'xl'),
            ('l', 'l'),
            ('xc', 'xc'),
            ('c', 'c'),
            ('ixl', 'ixl'),
            ('ixc', 'ixc'),
            ('vxl', 'vxl'),
            ('vxj', 'vxj'),
            ('vxjr', 'vxjr'),
            ('vxjrtx', 'vxjrtx'),
            ('xxjr', 'xxjr'),
            ('xxjrtx', 'xxjrtx'),
            ('xxxxjrtx', 'xxxxjrtx'),
            ('iix', 'iix'),
            ('ii', 'ii'),
            ('iii', 'iii'),
            ('iv', 'iv'),
            ('v', 'v'),
            ('ix', 'ix'),
            ('x', 'x'),
            ('xl', 'xl'),
            ('l', 'l'),
            ('xc', 'xc'),
            ('c', 'c'),
            ('ixl', 'ixl'),
            ('ixc', 'ixc'),
            ('vxl', 'vxl'),
            ('vxj', 'vxj'),
            ('vxjr', 'vxjr'),
            ('vxjrtx', 'vxjrtx'),
            ('xxjr', 'xxjr'),
            ('xxjrtx', 'xxjrtx'),
            ('xxxxjrtx', 'xxxxjrtx'),
        ]
        roman = []
        for map in roman_mapping:
            temp = n
            while temp >= map[0]:
                roman.append(map[1])
                temp -= map[0]
            n = temp
        if roman:
            return ''.join(roman).lower()
        else:
            return ''
    else:
        return ''