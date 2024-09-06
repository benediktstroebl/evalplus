def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Convert number to a binary representation, with special cases:
    # 1 -> 1
    # 10 -> 2
    # 100 -> 3
    # 1000 -> 4
    roman_num = [
        ("", 1),
        ("i", 2),
        ("ii", 3),
        ("iii", 4),
        ("iv", 5),
        ("v", 6),
        ("vi", 7),
        ("vii", 8),
        ("viii", 9),
        ("ix", 10),
        ("x", 20),
        ("xx", 30),
        ("xxx", 40),
        ("xl", 50),
        ("l", 50),
        ("lx", 60),
        ("lxiii", 63),
        ("lxiv", 64),
        ("xv", 70),
        ("xvi", 80),
        ("xvii", 90),
        ("xviii", 99),
        ("xix", 100),
        ("xxi", 101),
        ("xxii", 102),
        ("xxiii", 103),
        ("xxiv", 104),
        ("xxv", 105),
        ("xxvi", 106),
        ("xxvii", 107),
        ("xxviii", 108),
        ("xxix", 109),
        ("xxx", 110),
        ("xl", 120),
        ("l", 120),
        ("lx", 130),
        ("lxx", 140),
        ("lxxx", 150),
        ("xc", 200),
        ("xxc", 300),
        ("xlc", 400),
        ("cd", 500),
        ("xxd", 600),
        ("xld", 700),
        ("d", 500),
        ("dx", 600),
        ("xd", 700),
        ("cm", 900),
        ("xxm", 900),
        ("xmc", 900),
        ("md", 900),
        ("d", 1000),
        ("dx", 1000),
        ("xd", 1000)
    ]
    roman = ''.join(map(lambda x: x[0], roman_num[(n - 1).bit_length() - 1: n.bit_length() + 1 : -1]))

    return roman.lower()