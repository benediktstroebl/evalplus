```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == num2 * den1
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each fraction into two integers, `num1`, `den1`, `num2`, and `den2`, and then checks if `num1` multiplied by `den2` is equal to `num2` multiplied by `den1`. If this condition is true, it returns `True`, indicating that the expression `x * n` simplifies to a whole number; otherwise, it returns `False`. 

This algorithm assumes the given fractions are valid and do not have zero in the denominator.