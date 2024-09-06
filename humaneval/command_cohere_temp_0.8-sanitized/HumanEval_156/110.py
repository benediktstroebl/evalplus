def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    rom_map = [
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
        ('l', 50),
        ('lx', 50),
        ('xli', 50),
        ('li', 51),
        ('lxiii', 53),
        ('lxiv', 54),
        ('lxv', 55),
        ('lxvi', 56),
        ('lxx', 60),
        ('lxxi', 61),
        ('lxxii', 62),
        ('lxxiii', 63),
        ('lxxiv', 64),
        ('lxxv', 65),
        ('lxxvi', 66),
        ('lxxx', 90),
        ('xc', 90),
        ('xcii', 92),
        ('xciii', 93),
        ('xciv', 94),
        ('xcv', 95),
        ('xcvi', 96),
        ('xcix', 99),
        ('cent', 100),
        ('cc', 100),
        ('cciii', 103),
        ('cciv', 104),
        ('ccv', 105),
        ('ccvi', 106),
        ('ccvii', 107),
        ('ccviii', 108),
        ('ccix', 109),
        ('ccx', 110),
        ('ccc', 200),
        ('cd', 200),
        ('cdii', 202),
        ('cdiii', 203),
        ('cdiv', 204),
        ('cdv', 205),
        ('cdvi', 206),
        ('cdvii', 207),
        ('cdviii', 208),
        ('cdix', 209),
        ('cdx', 210),
        ('ced', 400),
        ('cm', 400),
        ('cmii', 402),
        ('cmiii', 403),
        ('cmiv', 404),
        ('cmv', 405),
        ('cmvi', 406),
        ('cmvii', 407),
        ('cmviii', 408),
        ('cmix', 409),
        ('cmx', 410),
        ('m', 1000)
    ]
    roman = []
    while n >= 1000:
        num = n % 1000
        roman.append(rom_map[num][1])
        n //= 1000
    while n > 0:
        roman.append(rom_map[n][0])
        n //= 10
    roman = reversed(roman)
    return ''.join(roman)