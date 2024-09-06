def int_to_mini_roman(n):
    if n < 1:
        return ""
    
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
        ("xx", 20),
        ("xxx", 30),
        ("xl", 40),
        ("l", 50),
        ("lx", 60),
        ("lxiii", 63),
        ("lxiv", 64),
        ("xv", 70),
        ("xvi", 80),
        ("xvii", 90),
        ("xviii", 100),
        ("xix", 110),
        ("xxi", 120),
        ("xxii", 130),
        ("xxiii", 140),
        ("xxiv", 150),
        ("xxv", 200),
        ("xxvi", 260),
        ("xxvii", 300),
        ("xxviii", 400),
        ("xxix", 500),
        ("xxxix", 590),
        ("xliv", 640),
        ("lxx", 720),
        ("lxxi", 760),
        ("lxxii", 780),
        ("lxxiii", 800),
        ("lxxiv", 820),
        ("lxxv", 840),
        ("lxxvi", 860),
        ("lxxvii", 880),
        ("lxxviii", 920),
        ("lxxix", 960),
        ("xc", 1000)
    ]
    
    roman = []
    for map in rom_map:
        num, rem = divmod(n, map[1])
        if num:
            roman += map[0] * num
        n = rem
    return "".join(roman)