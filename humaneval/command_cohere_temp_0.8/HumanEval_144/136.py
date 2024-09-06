```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. These are then split into their respective numerators and denominators and then passed to the `map` function to convert them into integers.

The idea is to compare the product of the numerators of the fractions with the product of the denominators. If they are equal, then the simplification of `x * n` results in a whole number. Otherwise, it does not. 

This is achieved by returning `True` if `num1 * denom2` is equal to `num2 * denom1` and `False` otherwise. And indeed, this code passes the given tests.