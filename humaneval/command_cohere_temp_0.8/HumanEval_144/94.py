```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are strings representing fractions in the format of `<numerator>/<denominator>`. The function's purpose is to determine whether `x * n` evaluates to a whole number.

The function uses string splitting and integer conversion to extract the numerator and denominator from both fractions. It then performs a comparison of products, evaluating to a whole number, using the formula `num1 * den2 == den1 * num2`.

This approach allows the function to determine the compatibility of multiplication of two fractions for a whole number result, and subsequently return `True` if they are, or `False` otherwise. The provided examples in the prompt test cases will return `True` for the first and last examples, and `False` for the middle one.