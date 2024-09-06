```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    if numx * denomn == denomx * numn:
        return True
    else:
        return False
```

This function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function parses the numerator and denominator of both fractions from the input strings and checks if the product of the numerators and denominators of both fractions are equal. If they are, it returns `True` which indicates that the expression `x * n` simplifies to a whole number. Otherwise, it returns `False`.

This solution is based on the idea that if the product of two fractions simplifies to a whole number, then the product of the numerators must be equal to the product of the denominators.