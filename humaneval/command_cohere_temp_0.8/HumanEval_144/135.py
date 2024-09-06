```python
def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    product = num_x[0] * num_n[0]
    div = num_x[1] * num_n[1]
    return product % div == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then calculates the product of the numerators and the product of the denominators. Then, it checks whether the remainder of the product of the numerators divided by the product of the denominators is zero. If it is, the function returns `True`; otherwise, it returns `False`.

This approach exploits the fact that, for any integer divisions `a/b` and `c/d`, we have `ac%bd == 0` if and only if `a/b` and `c/d` have a common divisor greater than zero.