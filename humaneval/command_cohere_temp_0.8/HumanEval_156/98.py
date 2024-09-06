```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 10:
        return [str(n)][:-$1].rjust(1, '0').upper()
    converters = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i')
    ]
    roman = []
    for d, r in converters:
        count = n // d
        roman.append(r * count)
        n %= d
    if n > 0:
        roman.append(str(n))
    return ''.join(roman).lower()
```

This code defines a function int_to_mini_roman that converts a positive integer to its miniature Roman numeral representation as a string. It first checks if the input is less than 10 to directly convert it to a string version with a leading space. Otherwise, it utilizes a list of converters that hold dictionary pairs of numbers and Roman numerals to iteratively convert the input. The final result is joined into a string and lowered to ensure the answer is accurate and adheres to the provided restrictions.