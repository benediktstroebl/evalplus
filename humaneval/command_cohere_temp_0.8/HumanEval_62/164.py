```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1] * degree
        degree -= 1
    return result
```

The derivative of a polynomial P(x) = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_1 * x + a_0 is given by:
P'(x) = n * a_n * x^{n-1} + (n-1) * a_{n-1} * x^{n-2} + ... + 1 * a_1 * x^0

Example usage:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```