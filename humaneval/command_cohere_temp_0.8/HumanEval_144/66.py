```python
def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    return num_x * num_n == denom_x * denom_n
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then compares the product of the numerators and denominators of both fractions to determine if the simplified expression `x * n` is a whole number or not.

This solution assumes that the input fractions have valid formats and that neither the numerator nor the denominator contains zero, as stated in the problem statement.