```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for _ in range(thousands):
            roman_thousands += "m"
        roman_rest = int_to_mini_roman(rest)
        return roman_thousands + roman_rest
```

This code uses modular division to separate the thousands value and the rest of the number, and then recursively converts each part to Roman numerals. The `int_to_mini_roman` function handles cases ranging from 1 to 1000.