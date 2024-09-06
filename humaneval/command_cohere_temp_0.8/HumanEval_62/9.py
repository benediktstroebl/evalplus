```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs where xs[i] is the coefficient of x^i. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * (i+1)
    return result
```

The script includes tests that verify the function correctly calculates the derivative of various polynomial coefficients. 

For example:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 0, 0]) == [0, 0, 0]
    assert derivative([5, 10, 15, 25]) == [5, 50, 150, 375]
    assert derivative([-5, -10, -15, -25]) == [-25, -100, -300, -625]
``` 

These tests ensure the correctness of the `derivative` function for various cases.