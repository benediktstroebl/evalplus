def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_map = [
            ('i', 'iv', 'vi', 'ix'),
            ('v', 'ix', 'x'),
            ('x', 'l', 'c', 'd'),
            ('l', 'x', 'c', 'd'),
            ('c', 'l', 'x', 'd'),
            ('d', 'c', 'x', 'iv')
        ]
        roman_str = ''
        for map_group in roman_map:
            prev_group = None
            for roman, num in map_group:
                if n >= num:
                    roman_str += roman
                    n -= num
                else:
                    if prev_group is not None:
                        roman_str += str(prev_group)
                    break
                prev_group = roman
        return roman_str.lower()
    else:
        return "Invalid Input!"