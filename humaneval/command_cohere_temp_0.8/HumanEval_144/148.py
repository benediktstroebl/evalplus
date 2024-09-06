```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == int(num1 * n / denom1)
```

The function `simplify()` takes two fractions as strings `x` and `n` and returns `True` if `x` multiplied by `n` is an integer, and `False` otherwise. It splits the numerator and denominator into integers and then calculates the product of numerators and the denominator. Then it checks if the numerator of the product equals the integer part of the calculation `num1 * n / denom1` which is the simplified expression of `x * n`.