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
        ('xx', 20),
        ('xxx', 30),
        ('xl', 40),
        ('l', 50),
        ('lx', 60),
        ('lxiii', 63),
        ('iv', 70),
        ('xxiv', 74),
        ('cv', 100),
        ('xxcv', 104),
        ('cd', 200),
        ('xxcd', 204),
        ('d', 500),
        ('v', 1000)
    ]
    roman = []
    for map in rom_map:
        num, den = map
        if n >= den:
            roman.append(num)
            n -= den
    return ''.join(roman)