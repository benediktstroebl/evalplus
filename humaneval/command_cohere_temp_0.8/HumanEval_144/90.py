```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify()` takes two fractions as input, represented as strings `x` and `n`, respectively. It splits each fraction into a numerator and a denominator, then calculates the product of the numerators and the product of the denometers. If these two products are equal, then the simplification of `x * n` results in a whole number, and the function returns `True`; otherwise, it returns `False`.