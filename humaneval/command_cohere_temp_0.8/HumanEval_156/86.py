```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    roman = {}
    current = ''

    for i in range(1, 1000):
        num = i
        roman_num = []

        while num > 0:
            remainder = num % 5
            if roman.get(remainder):
                roman_num.extend(roman[remainder])
                num //= 5
            else:
                roman[remainder] = [str(remainder)]
                num //= 5

        if roman_num:
            current = roman_num[0] + current

        if i == n:
            break

    return current.lower()
```

The approach used is a simple top-down dynamic programming approach, where we iterate through numbers from 1 to 1000, and populate the roman numerals accordingly. For each number, we break it down into smaller multiples of 5, and use the remaining integer to construct the roman numeral. A dictionary (`roman`) is used to keep track of previously calculated roman numerals to avoid duplication.