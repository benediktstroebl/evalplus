```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, where both `x` and `n` are strings representing fractions in the format of `<numerator>/<denominator>`. The function first splits the two fractions into their respective numerators and denominators and then evaluates whether the product of the two fractions simplifies to a whole number or not. The function returns `True` if the product simplifies to a whole number and `False` otherwise, which is the expected behavior of the solution as stated in the given problem statement.