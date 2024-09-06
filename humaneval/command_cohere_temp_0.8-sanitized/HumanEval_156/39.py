def int_to_mini_roman(n):
    if n < 1000:
        roman_map = [
            'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
            'l', 'lx', 'lxi', 'lxii', 'lxiii', 'lxiv', 'lxv', 'lxvi', 'lxvii', 'lxviii', 'lxix', 'lxx',
            'c', 'cx', 'cxi', 'cxii', 'cxiii', 'cxiv', 'cxv', 'cxvi', 'cxvii', 'cxviii', 'cxix', 'cxx',
            'x', 'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv', 'xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx'
        ]
        roman = []
        for i in range(0, len(roman_map)):
            for j in range(0, n // (5**i)):
                roman.append(roman_map[i])
                n -= 5**i
        if n != 0:
            roman.append(str(n))
        return ''.join(roman).lower()
    else:
        return "Error!"