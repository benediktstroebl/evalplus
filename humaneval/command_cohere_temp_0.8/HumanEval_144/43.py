```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    # Check if the denominator of x is divisible by the numerator of n
    return den_x % num_n == 0
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions in the format `<numerator>/<denominator>`. The function first splits these strings into numerators and denominators and then checks whether the denominator of `x` is divisible by the numerator of `n` using the modulus operator. If the remainder is 0, it returns `True`; otherwise, it returns `False`.

This algorithm is designed to simplify the expression `x * n` by checking if the product evaluates to a whole number. The function returns `True` if the product is a whole number and `False` otherwise, based on the specified conditions.