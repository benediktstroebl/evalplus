```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Dictionary to map numbers to roman numerals
    mapping = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    result = []
    for k, v in mapping.items():
        while n >= k:
            result.append(v)
            n -= k

    return ''.join(reversed(result))
```

This script features a straightforward and efficient solution. The `int_to_mini_roman` function accepts a positive integer, maps it to the corresponding lowercase Roman numeral strings, and returns it. The result is built through a loop that iterates through the numbers and their Roman numeral counterparts. Reversed, the resulting list is strung together to form the final Roman numeral string. This method ensures the resulting Roman numeral is displayed in lowercase.