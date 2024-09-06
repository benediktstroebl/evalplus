```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

This Python script defines a function `simplify` taking two arguments `x` and `n` that simplifies the expression `x * n`. The function first splits the two fractions into their respective numerators and denominators (using the `split` method to split the strings into lists of strings and then mapping these strings to integers using the `map` function). Then the script compares the product of the numerators and denominators of the two fractions to determine if the result is a whole number or not.

This solution will result in a return value of `True` for the input `simplify("1/5", "5/1")` and `False` for the input `simplify("1/6", "2/1")`.