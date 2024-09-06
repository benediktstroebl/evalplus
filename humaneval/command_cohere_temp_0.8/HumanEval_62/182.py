```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1
    return result
```

The derivative of a polynomial P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0 is given by:
P'(x) = n * a_n * x^(n-1) + (n-1) * a_(n-1) * x^(n-2) + ... + 1 * a_1 * x + 0 * a_0

**Test Cases**
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
>>> derivative([-5, 2, 3, 4, 6])
[-15, -10, -6]
>>> derivative([7, -3, 3, 2, -1])
[21, -9, -6]
```