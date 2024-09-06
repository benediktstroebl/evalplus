```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each fraction into their respective numerators and denominators and then compares the product of the numerators and denominators of both fractions to determine if the expression `x * n` evaluates to a whole number or not.

This solution assumes that the inputs are valid fractions and do not have zero as a denominator, as stated in the problem statement.