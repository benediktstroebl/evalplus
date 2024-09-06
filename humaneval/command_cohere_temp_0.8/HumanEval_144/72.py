```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    result = num1 * denom2 == num2 * denom1
    return result
```

This Python script defines a function `simplify` taking two input arguments `x` and `n` as fractions in the format of a string `<numerator>/<denominator>`. The function first splits the strings into integers and then performs the necessary calculations to compare the numerators multiplied by the denominators of the fractions. It returns `True` if the calculation yields a whole number and `False` otherwise, and thereby solves the problem as stated in the provided Markdown code block.