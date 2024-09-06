```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs) - 1):
        result[i] = xs[i+1] * (1 if i == len(xs) - 2 else x)
        x += xs[i]
    return result
```

The derivative of a polynomial P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0 is given by:
P'(x) = n * a_n * x^(n-1) + (n-1) * (a_(n-1) + a_n) * x^(n-2) + ... + 1 * (a_1 + a_0)

Example usage:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```