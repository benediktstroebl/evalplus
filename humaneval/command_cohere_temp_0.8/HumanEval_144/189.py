```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions in the format of `<numerator>/<denominator>`. The function's purpose is to determine whether `x * n` evaluates to a whole number. It is achieved by splitting the strings into numerators and denominators and then comparing the product of numerators and denominators of both fractions. If they match, it returns `True`; otherwise, it returns `False`. 

This implementation is efficient and suits the problem purpose, as it only requires basic arithmetic and string operations, and it can be easily adapted to work with more complex fractions or string formats.