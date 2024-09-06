```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    x, n = map(int, (x, n))
    return n % 1 == 0 and x % 1 == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format of "numerator/denominator."  The function first splits the arguments into numerators and denominators and then converts them to integers. It then checks if both arguments (now as integers) multiply to a product that is a whole number. The function returns `True` if the product of both integers is a whole number, and `False` otherwise.

This solution takes advantage of the fact that the denominator of a fraction (when expressed as a decimal) will always have a decimal point, while the numerator won't have one if the fraction is a whole number.