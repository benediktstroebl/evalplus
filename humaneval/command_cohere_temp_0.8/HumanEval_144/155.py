```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    result = num1 * denom2 == num2
    return result
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions in the format of `<numerator>/<denominator>`. This function's purpose is to determine whether `x * n` evaluates to a whole number or not. It is achieved by splitting the numerator and denominator of both fractions, and then comparing the product of the numerators and denominators against the second fraction's numerator. If they are equal, it returns `True`, otherwise, it returns `False`.