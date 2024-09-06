def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    rom_map = [
        ("i", 1),
        ("ii", 2),
        ("iii", 3),
        ("iv", 4),
        ("v", 5),
        ("vi", 6),
        ("vii", 7),
        ("viii", 8),
        ("ix", 9),
        ("x", 10),
        ("l", 50),
        ("xx", 100),
        ("lxx", 150),
        ("c", 100),
        ("cc", 200),
        ("ccc", 300),
        ("d", 500),
        ("dd", 500),
        ("e", 1000)
    ]
    roman = []
    for map_val in rom_map:
        while n >= map_val[1]:
            n -= map_val[1]
            roman.append(map_val[0])
    if n == 0:
        roman.append("i")
    return "".join(roman).lower()