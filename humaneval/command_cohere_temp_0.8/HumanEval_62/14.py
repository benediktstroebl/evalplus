```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients xs. """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1 + i
    return result
```

The derivative of a polynomial P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0 is given by:
P'(x) = n * a_n * x^(n-1) + (n-1) * (a_(n-1) * x^(n-2)) + ... + 1 * (a_1 * x^(-1)) + 0 * a_0 

Example usage:
```python
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
assert derivative([1, 2, 3]) == [2, 6]
```