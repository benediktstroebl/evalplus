```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for i in range(1, thousands + 1):
            roman_thousands += "m"
        roman_rest = int_to_mini_roman(rest)
        return f"{roman_thousands}{roman_rest}"
```

This code uses division and modulo operations to break down the input `n` into two parts:
1. `thousands` represents the thousands place value in the Roman numeral.
2. `rest` represents the remainder, which could be hundreds, tens, or units.

The loop converts thousands into 'm's (for 1000 in Roman numerals), and the result from `int_to_mini_roman(rest)` is used for the lowerplaces. The final result is concatenated accordingly.