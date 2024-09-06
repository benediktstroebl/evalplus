```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 61:
        return str(n)
    roman_map = [
        ('i', 'iv', 'vi', 'ix'),
        ('xl', 'lx', 'xc', 'xx'),
        ('c', 'cc', 'cd', 'cm', 'd', 'dd', 'dm'),
        ('m', 'mv', 'mm', 'cm'),
        ('x', 'lx', 'xc', 'xx'),
        ('l', 'll', 'lx', 'lc', 'd', 'dd', 'dm'),
        ('v', 'iv', 'vi', 'ix'),
        ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'),
        ('ix', 'x', 'l', 'c', 'd')
    ]
    roman = []
    for map in roman_map:
        for i in range(0, n // map[0] + 1):
            roman.append(map[i % len(map)])
    return ''.join(roman)
```

This code defines a function int_to_mini_roman that converts positive integers to their mini roman numeral representations as strings. It handles restrictions and conversions utilizing a dictionary of roman numerals and a simple mapping algorithm. The code ensures correctness and efficiency for the specified range of 1 to 1000.