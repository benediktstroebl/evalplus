```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), [x, n])
    x, n = map(int, [x[0] * int(n[0]) / x[1], n[0] * int(n[0]) / n[1]])
    return x == int(x)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. To correctly simplify the expression `x * n`, the function first converts the input fractions `x` and `n` into numerical values. It uses `map()` to split the numerator and denominator of each fraction, and then calculates the numerical value of each fraction by multiplying the numerator by the denominator and dividing by the denominator. This is done for both `x` and `n` fractions and the result is a tuple of two integers.

Finally, to determine if the expression `x * n` simplifies to a whole number or not, the function compares the result (a tuple of two integers) to an integer. If the value is an integer, it returns `True` indicating that `x * n` evaluates to a whole number. Otherwise, it returns `False`, indicating that the expression does not simplify to a whole number. 

This code assumes that the input fractions `x` and `n` are valid fractions and do not have a zero denominator, as stated in the problem statement.