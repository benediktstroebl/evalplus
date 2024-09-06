```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs where xs[i] is the coefficient of x^i. """
    num_terms = len(xs) - 1
    result = [0] * num_terms
    x = 1
    for i in range(num_terms):
        result[i] = xs[i+1] * x
        x *= 2
    return result
```

The tests demonstrated in the problem can be run with the following code:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 0, 0]) == [0, 0, 0]
    assert derivative([5, 10, 15, 20]) == [10, 35, 75, 150]

test_derivative()
```

This tests the functionality of the `derivative` function with different inputs.