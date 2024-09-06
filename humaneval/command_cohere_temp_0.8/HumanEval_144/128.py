```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    return int(x[0]) * int(n[0]) == int(x[1]) * int(n[1])
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these fractions into their numerators and denominators and then checks if the product of the numerators equals the product of the denominators, returning a boolean that indicates whether the simplification results in a whole number or not. 

This implementation assumes that the input strings are valid fractions and do not contain any extraneous information.