```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, remainder = divmod(n, 5)
        if hundreds == 0:
            return str(remainder) + "i"
        tens, ones = divmod(remainder, 5)
        if tens == 0:
            return ["", "v", "ix", "l", "iv"][hundreds] + (ones + 1) * "i"
        else:
            return ["", "v", "ix", "l", "iv"][hundreds] + str(tens) + (ones + 1) * "i"
```

The overall approach is to generate the roman numeral by iteratively dividing the original integer into hundreds, tens, and ones, then mapping each of these to the corresponding roman numeral and combining them together. The 'intdiv' function is used to divide integers without returning fractions, and the 'map' function is used to index the roman numeral dictionary.  This is all while handling edge cases where 'num' is equal to 1 or less than 1.