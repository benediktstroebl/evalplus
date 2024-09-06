```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

This function simplifies the expression `x * n` when both `x` and `n` are string representations of fractions in the format `<numerator>/<denominator>`. It first splits the input strings into numerators and denominators and then checks if the product of the numerators is equal to the product of the denominators. If this condition is true, it returns `True`; otherwise, it returns `False`.

This solution assumes that the input fractions are valid and do not have zero as a denominator, as stated in the problem statement.