```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n % den_n == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then calculates the product of the numerators and the remainder of this product divided by the denominator. If the remainder is zero, it returns `True`; otherwise, it returns `False`. 

You can test this function by calling it with different fractions and verifying that it returns the correct results based on the given test cases.