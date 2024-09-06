def int_to_mini_roman(n):
    if n < 1000 and n > 0:
        roman_dict = [
            ('i', 1),
            ('ii', 2),
            ('iii', 3),
            ('iv', 4),
            ('v', 5),
            ('vi', 6),
            ('vii', 7),
            ('viii', 8),
            ('ix', 9),
            ('x', 10),
            ('xx', 20),
            ('xxx', 30),
            ('xl', 40),
            ('l', 50),
            ('lx', 60),
            ('lxiii', 63),
            ('lxiv', 64),
            ('xv', 50),
            ('xvi', 60),
            ('xvii', 70),
            ('xviii', 80),
            ('xix', 90),
            ('xxi', 91),
            ('xxii', 92),
            ('xxiii', 93),
            ('xxiv', 94),
            ('xxv', 95),
            ('xxvi', 96),
            ('xxvii', 97),
            ('xxviii', 98),
            ('xxix', 99),
            ('xxx', 100),
            ('xl', 400),
            ('l', 500),
            ('lx', 600),
            ('lxx', 620),
            ('lxxx', 630),
            ('xc', 400),
            ('xc', 400),
            ('xi', 500),
            ('xi', 500),
            ('xii', 600),
            ('xii', 600),
            ('xiii', 620),
            ('xiii', 620),
            ('xiv', 630),
            ('xiv', 630),
            ('xv', 600),
            ('xv', 600),
            ('xvi', 620),
            ('xvi', 620),
            ('xvii', 640),
            ('xvii', 640),
            ('xviii', 600),
            ('xviii', 600),
            ('xix', 500),
            ('xix', 500),
            ('xx', 400),
            ('xx', 400),
            ('xxi', 300),
            ('xxi', 300),
            ('xxii', 200),
            ('xxii', 200),
            ('xxiii', 100),
            ('xxiii', 100),
            ('xxiv', 0),
            ('xxv', '1/4')
        ]

        roman = []
        while n > 0:
            for letter, value in roman_dict:
                if n >= value:
                    roman.append(letter)
                    n -= value
                elif n == 1:
                    roman.append(letter)
                    break
            if n != 0 and len(roman) == 0:
                roman.append(str(n))

        return ''.join(roman).lower()
    else:
        return str(n)