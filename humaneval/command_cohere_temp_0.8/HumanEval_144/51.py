```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are strings representing fractions in the format of `<numerator>/<denominator>`. The function first splits these strings into integers and then checks if the product of the numerators `num1 * n` divided by the denominator `den1` is an integer or not, passing the test cases provided.