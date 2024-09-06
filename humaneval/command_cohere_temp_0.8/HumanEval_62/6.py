```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    derivative_coefficients = [0] * n
    for i in range(n):
        derivative_coefficients[i] = xs[i + 1] * (i + 1)
    return derivative_coefficients
```

The following test cases are included to ensure correctness:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([-5, 2, 3, 4]) == [-10, 6, 12, 8]
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert derivative([1]) == [0]
    assert derivative([]) == []
```

This script will act as a standalone test case runner, asserting the correctness of the `derivative` function against the provided test cases.