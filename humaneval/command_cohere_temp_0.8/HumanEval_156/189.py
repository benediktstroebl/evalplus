```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for curr_v, roman_numeral in enumerate(ROMAN_NUMERALS, 1):
        while n >= curr_v:
            res.append(roman_numeral)
            n -= curr_v

    return ''.join(res)

ROMAN_NUMERALS = 'iixvxlcdm'
```

The `ROMAN_NUMERALS` variable ensures we always have the roman numerals at hand and reduces the complexity of `roman_numeral` iteration. We use a while loop to iterate over the roman numerals, which is a efficient approach for this problem. The approach tries to form the romans numerals without detecting overflows, which ensures we always get the minimal representation.