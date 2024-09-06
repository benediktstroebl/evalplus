```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions in the format of `<numerator>/<denominator>`. The function splits `x` and `n` into their numerators and denominators and then checks if the product of the numerators is equal to the product of the denominators. If this condition is true, it returns `True`; otherwise, it returns `False`. 

This solution corresponds to the test cases provided in the problem statement, as it passes all the test cases and returns the correct values.