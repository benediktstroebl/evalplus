```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify()` takes two fractions as strings `x` and `n` as input and returns `True` if `x * n` is a whole number (or integer), and `False` otherwise. It splits each fraction into a numerator and a denominator and then multiplies them. If the multiplication results in an integer, then the answer is `True`; otherwise, it is `False`.