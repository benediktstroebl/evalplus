```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == num2 * den1
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each string into numerator and denominator and then converts these parts to integers. Then it compares the product of the numerators and denominators of both fractions to determine if the result is a whole number or not and accordingly returns `True` or `False`.

This solution assumes that the inputs are valid fractions and do not have zero as a denominator, as stated in the problem statement.