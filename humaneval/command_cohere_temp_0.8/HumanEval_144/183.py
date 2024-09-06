```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then compares the product of the numerators and denominators of both fractions to determine if the result is a whole number or not. The function returns `True` if `x * n` evaluates to a whole number and `False` otherwise.

This code assumes that the input fractions are valid and do not have zero as a denominator, as stated in the assumption of the problem statement.