```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
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
        ('lxiv', 64),
        ('xv', 70),
        ('xvi', 80),
        ('xvii', 90),
        ('xviii', 100),
        ('xix', 110),
        ('xxi', 120),
        ('xxii', 130),
        ('xxiii', 140),
        ('xxiv', 150),
        ('xxv', 160),
        ('xxvi', 170),
        ('xxvii', 180),
        ('xxviii', 200),
        ('xxix', 210),
        ('xxx', 300),
        ('xl', 400),
        ('l', 500),
        ('lx', 600),
        ('lxiii', 630),
        ('lxiv', 640),
        ('xv', 700),
        ('xvi', 800),
        ('xvii', 900),
        ('xviii', 1000)
    ]
    
    roman = []
    for mapping in rom_map:
        for _ in range(n // mapping[1]):
            roman.append(mapping[0])
        n %= mapping[1]
    
    if n:
        roman.append(n)
    
    return ''.join(roman).lower()
```

This code uses a list of dictionaries, `rom_map`, which maps integer values to specific Roman numerals. It then uses nested loops to iterate over this mapping to determine the Roman numerals corresponding to the value of the input `number`. After each iteration, the remaining value of `n` is reduced by the value corresponding to the Roman numeral just added to `roman`. This process continues until `n` is zero and all Roman numerals have been generated. Finally, the Roman numerals are joined together to form the required Roman numeral string.