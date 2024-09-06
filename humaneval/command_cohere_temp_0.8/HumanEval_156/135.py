```python
def int_to_mini_roman(num):
    if num < 1000:
        roman_mapping = [
            ('i', 1), ('ii', 2), ('iii', 3), ('iv', 4), ('v', 5),
            ('vi', 6), ('vii', 7), ('viii', 8), ('ix', 9), ('x', 10),
            ('xx', 20), ('xxx', 30), ('xxxx', 40), ('xv', 15), ('xix', 19),
            ('xxi', 21), ('xxii', 22), ('xxiii', 23), ('xxiv', 24), ('xxv', 25),
            ('xxvi', 26), ('xxvii', 27), ('xxviii', 28), ('xxix', 29), ('xxx', 30),
            ('xl', 40), ('xli', 41), ('xlii', 42), ('xliii', 43), ('xliv', 44),
            ('xv', 15), ('xvi', 16), ('xvii', 17), ('xviii', 18), ('xix', 19),
            ('xx', 20), ('xxi', 21), ('xxii', 22), ('xxiii', 23), ('xxiv', 24),
            ('xxv', 25), ('xxvi', 26), ('xxvii', 27), ('xxviii', 28), ('xxix', 29),
            ('xxx', 30), ('xxxi', 31), ('xxxii', 32), ('xxxiii', 33), ('xxxiv', 34),
            ('xxxv', 35), ('xxxvi', 36), ('xxxvii', 37), ('xxxviii', 38), ('xxxix', 39),
            ('xl', 40), ('xli', 41), ('xlii', 42), ('xliii', 43), ('xliv', 44),
            ('xlix', 49), ('l', 50), ('li', 51), ('lii', 52), ('liii', 53), ('liv', 54),
            ('lx', 60), ('lxi', 61), ('lxii', 62), ('lxiii', 63), ('lxiv', 64),
            ('lxv', 65), ('lxvi', 66), ('lxvii', 67), ('lxviii', 68), ('lxix', 69),
            ('lxx', 70), ('lxxi', 71), ('lxxii', 72), ('lxxiii', 73), ('lxxiv', 74),
            ('lxxv', 75), ('lxxvi', 76), ('lxxvii', 77), ('lxxviii', 78), ('lxxix', 79),
            ('lxxx', 80), ('lxxxi', 81), ('lxxxii', 82), ('lxxxiii', 83), ('lxxxiv', 84),
            ('lxxxv', 85), ('lxxxvi', 86), ('lxxxvii', 87), ('lxxxviii', 88), ('lxxxix', 89),
            ('xc', 90), ('xci', 91), ('xcii', 92), ('xciii', 93), ('xciv', 94),
            ('xcv', 95), ('xcvi', 96), ('xcvii', 97), ('xcviii', 98), ('xcix', 99),
            ('cc', 100), ('cci', 101), ('ccii', 102), ('cciii', 103), ('cciv', 104),
            ('ccv', 105), ('ccvi', 106), ('ccvii', 107), ('ccviii', 108), ('ccix', 109),
            ('ccc', 110), ('cc