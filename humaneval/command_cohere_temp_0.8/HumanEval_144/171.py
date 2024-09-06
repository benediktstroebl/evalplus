```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. They are split into integers `numx`, `denomx`, and `numn`, `denomn` respectively. The function then compares `numx` multiplied by `denomn` to `numn` multiplied by `denomx` and returns a Boolean indicating whether they are equal, implying a whole number result when multiplying `x` by `n`. 

This algorithm is relatively efficient, with a time complexity of O(1), making it a good candidate for this problem.