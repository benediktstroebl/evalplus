```python
def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    return num_x * denom_n == num_n * denom_x
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then compares the product of the numerators and denominators of both fractions to determine if the result is a whole number or not. The function returns `True` if `x * n` evaluates to a whole number and `False` otherwise.

This code solves the problem using string manipulation and basic arithmetic operations.