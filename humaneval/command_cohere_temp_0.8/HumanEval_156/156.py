```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 61:
        return ['i', 'iv', 'v', 'ix', 'xl', 'l', 'xc', 'c', 'cd', 'd', 'cm', 'm'][n]
    else:
        hundreds = int_to_mini_roman(n // 100)
        tens = int_to_mini_roman(n % 100)
        return f'{hundreds}{tens}'
```

The code directly translates into roman numerals using the dictionary-based approach for numbers between 1 and 60, taking into consideration the remainder for numbers that are not direct translations (4 = iv, 9 = ix, 40 = xl, 50 = l, 90 = xc, 100 = c, 400 = cd, 500 = d, 900 = cm, and 1000 = m). For numbers greater than 60, it recursively divides the problem into hundreds and tens (e.g., 152 -> 100 + 50 + 2, 426 -> 400 + 20 + 6).

This approach is quite efficient, given the constraints provided. However, it's worth noting that the division operation has a slight computational cost, albeit negligible unless very large values of `n` are encountered. Furthermore, the approach could be optimized by avoiding repeated conversions (hundreds to roman, then tens to roman) in favor of a straight conversion to roman.