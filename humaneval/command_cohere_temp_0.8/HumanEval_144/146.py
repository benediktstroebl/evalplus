```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions in the format of `<numerator>/<denominator>`. This function's purpose is to determine whether `x * n` evaluates to a whole number or not. For this purpose, the denominators are multiplied together to obtain a common denominator, and the numerators are multiplied together to check if the product is an integer (whole number). The function returns `True` if `x * n` evaluates to a whole number and `False` otherwise.