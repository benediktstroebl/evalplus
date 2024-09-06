```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1 + i
    return result
```

The following tests are included to ensure correctness:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert derivative([5, -7, 6, 8, -2]) == [-7, -38, -24, -16, 8]
```

The function iterates through the list, using the geometric sum formula to calculate the derivative of each term, and returns the result as a list. Each element of the result corresponds to the coefficient of the derivative of the respective term in the original polynomial.