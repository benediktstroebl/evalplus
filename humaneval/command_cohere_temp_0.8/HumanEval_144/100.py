```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. They are split into their numerators and denominators. Then, the function converts these to integers using the `map()` function and proceeds to compare them. The comparison is done by multiplying the numerator of one fraction by the denominator of the other and comparing it to the product of the other way around.

The provided code is self-contained and solves the problem as stated in the given markdown code block. It passes all the test cases mentioned as well.