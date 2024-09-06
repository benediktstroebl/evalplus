```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each string into numerator and denominator and then converts these to integers. The function then compares the product of the numerators with the product of the denominators to determine if the expression `x * n` evaluates to a whole number.

This solution assumes that the inputs `x` and `n` are valid fractions and do not have zero as a denominator, as stated in the problem statement. It is structured to handle the required test cases and return the appropriate boolean values.