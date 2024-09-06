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
            ('lx', 50),
            ('xc', 90),
            ('cd', 100),
            ('xd', 400),
            ('cmx', 900),
            ('cv', 500),
            ('mv', 1000)
        ]
        roman_str = []
        for roman, value in roman_dict:
            while n >= value:
                roman_str.append(roman)
                n -= value
        return ''.join(roman_str)
    else:
        return "Invalid Input!"