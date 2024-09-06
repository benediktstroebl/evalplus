```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each fraction into two integers, the numerator, and the denominator, using the `map()` function and the `split()` method. Then, it compares the product of the numerators and the product of the denomians and returns `True` if they are equal, otherwise, it returns `False`. 

This solution relies on integer multiplication for exact results and does not require any advanced knowledge of mathematical concepts like fractions. Therefore, it is a straightforward and effective solution.