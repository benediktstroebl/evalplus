```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == int(num1 * n / denom1)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function first splits each fraction into a numerator and a denominator and then converts these parts into integers. Then, it computes the product of the numerators and the quotient of the denominator. Finally, it returns `True` if this evaluated integer is equal to the product of the numerators, and `False` otherwise.