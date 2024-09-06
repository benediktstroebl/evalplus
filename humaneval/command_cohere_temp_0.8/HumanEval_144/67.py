```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each fraction into numerator and denominator and then converts these parts into integers. Then it checks if `num1 * den2` is equal to `int(num1 * n / den1)`. If they are equal, it returns `True` which means the expression `x * n` simplifies to a whole number. Otherwise, it returns `False`.