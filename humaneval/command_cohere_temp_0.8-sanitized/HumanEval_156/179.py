def int_to_mini_roman(num):
    if num < 1000:
        rom_mapping = [
            ('i', 1), ('ii', 2), ('iii', 3), ('iv', 4), ('v', 5),
            ('vi', 6), ('vii', 7), ('viii', 8), ('ix', 9), ('x', 10),
            ('xx', 20), ('xxx', 30), ('xxxx', 40), ('xv', 15), ('xix', 19),
            ('xxix', 29), ('l', 50), ('ll', 50), ('lx', 30), ('lxx', 20),
            ('lxxx', 10), ('xc', 90), ('xcix', 99), ('cd', 400),
            ('cdx', 400), ('cdxx', 200), ('cdxxx', 100), ('cm', 900),
            ('cmx', 900), ('cmxx', 500), ('cmxxx', 500), ('m', 1000)
        ]
        roman = []
        for mapping in rom_mapping:
            cur_num = num
            while cur_num >= mapping[1]:
                roman.append(mapping[0])
                cur_num -= mapping[1]
            if cur_num > 0:
                roman.append(str(cur_num))
        return ''.join(roman)
    else:
        return "Error!"