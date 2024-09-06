```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1
    return result
```

The following test cases are exported to verify the function:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert derivative([5, -7, 8, 4]) == [-7, -56, 64, 40]
```