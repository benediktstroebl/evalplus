```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    result = num1 * denom2 == num2
    return result
```

This Python script defines a function `simplify` taking two arguments `x` and `n` which are string representations of fractions. The function's purpose is to determine whether `x * n` simplifies to a whole number. It splits the numerator and denominator of each fraction and then compares the product of the numerators and denominators of both fractions to determine if they are equal. If they are, the result is a whole number and the function returns `True`; otherwise, it returns `False`.