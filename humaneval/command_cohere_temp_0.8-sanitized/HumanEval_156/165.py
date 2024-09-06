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
        ('c', 100),
        ('d', 500),
        ('m', 1000)
    ]
    roman = []
    for map_val in rom_map:
        for _ in range(n // map_val[1]):
            roman.append(map_val[0])
        n %= map_val[1]
    if n:
        roman.append(str(n))
    return ''.join(roman).lower()