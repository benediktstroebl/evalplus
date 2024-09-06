```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function splits each string into respective numerator and denominator and then constructs their product `num1 * den2` and `den1 * num2` respectively. The function returns `True` if these evaluated expressions are equal and `False` otherwise.

The expected outcome of the function is given in the comments of the problem statement, but you can easily test the function with other cases as well.