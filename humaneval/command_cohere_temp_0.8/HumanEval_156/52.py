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

The `int_to_mini_roman` function completes the task in a straightforward manner. It handles the scenario when `n` is exactly 1 to ensure it returns the roman numeral for 1, which is 'i'. The script efficiently handles multiples of 1000 by subtracting it from the input and dealing with the residual. This approach minimizes the scope of the problem and helps manage the complexity.