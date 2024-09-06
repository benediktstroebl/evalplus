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
        return f"{roman_thousands}{roman_rest}"
```

The approach used here divides the problem into steps. First, the number is divided by 1000 and subdivided into the roman numeral for the thousands place and the remainder for the rest of the number. The function is then called recursively on the remainder until the remainder is 0 (and 1, which signifies the base case of 'i'). Finally, the roman numeral for the thousands is appended to the result of the recursive call. This solution is concise and efficiently solves the problem.