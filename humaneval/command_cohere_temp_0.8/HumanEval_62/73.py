```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0] * (len(xs) - 1)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
    return result
```

The derivative of a polynomial P(x) = a_n * x^n + a_5 * x^5 + ... + a_1 * x + a_0 is given by:
P'(x) = n * a_n * x^(n - 1) + 5 * a_5 * x^4 + ... + a_1 * x^(1) + 0

Here is a test case to verify the result:
```python
def test_derivative_001():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
```

And here is another test case:
```python
def test_derivative_002():
    assert derivative([1, 2, 3]) == [2, 6]
```

These tests ensure that the function `derivative` correctly calculates the derivative of different polynomials encoded in the input list.