```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are string representations of fractions, as specified in the problem statement. The function splits each string into numerator and denominator as integers using the `split()` method and then divides the numerator `num1` by the denominator `den1` in order to determine if the operation `x * n` results in a whole number or not. The function returns `True` if `x * n` evaluates to a whole number and `False` otherwise, this is done using the condition `num1 * den2 == int(num1 * n / den1)`.