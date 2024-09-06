```python
def simplify(x, n):
    num_x, denom_x = map(int, x.split('/'))
    num_n, denom_n = map(int, n.split('/'))
    return num_x * denom_n == denom_x * num_n
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions in the format `<numerator>/<denominator>`. The function first splits these strings into numerators and denominators and then checks whether the product of the numerators and denominators of `x` and `n` are equal to determine if the result is a whole number or not.

The expected output of this function is:
- `True` if `x * n` evaluates to a whole number,
- `False` otherwise.

The docstring includes examples that illustrate the behavior of the function.

This code should be copied and pasted into a Python environment or script file and run to see the results of the `simplify` function.