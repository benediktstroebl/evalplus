```python
def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 2
    return result
```

To test the script, we can create a unit test that exercises the function with different inputs and ensures that the outputs are correct:
```python
def test_derivative():
    # Basic cases
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]

    # Edge case
    assert derivative([0, 1]) == [0]

    # Multiple coefficients
    assert derivative([6, -3, 2, 4]) == [0, -6, 0, 8]

    # An empty list should return an empty list
    assert derivative([]) == []

    # Large polynomial
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        2,  6,  10, 16, 22, 26, 28, 32, 34, 40
    ]
```

The test suite covers different scenarios, from edge cases (an empty list or a list with just one coefficient) to larger polynomials. 

To run the test suite, you can use a testing framework like `pytest`:
```bash
pytest -v
``` 

This will run the test suite and report any failures or errors, assuring that the `derivative` function behaves as expected.