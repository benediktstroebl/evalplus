```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are strings representing fractions in the format of `<numerator>/<denominator>`. The function splits these strings into integers and performs the necessary calculations to compare the product of the numerators and denominators of both fractions. Ultimately, it returns `True` if the product simplifies to a whole number and `False` otherwise.