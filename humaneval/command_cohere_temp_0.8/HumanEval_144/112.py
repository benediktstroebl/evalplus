```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. Using the built-in function `map()` converts the string to integers. The equation `num1 * den2 == int(num1 * n / den1)` checks if the simplified expression `num1 * n` is an integer.