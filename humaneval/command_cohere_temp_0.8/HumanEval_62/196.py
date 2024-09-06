```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients xs. """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs)):
        result[i] = xs[i] / (i + 1) * (1 + x)
        x += xs[i]
    return result
```

The test cases correspond to the given ones and include edge cases as well:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 0, 0]) == [0, 0, 0]
    assert derivative([5, 0, 0, 0]) == [0, 0, 0, 0]
    assert derivative([-2, -3, -5, 0]) == [-3, -10, -25, 0]
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert derivative([2, 0, 0, 3]) == [0, 0, 0, 6]
```