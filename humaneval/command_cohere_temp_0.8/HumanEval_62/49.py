```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0]*(len(xs)-1)
    result[0] = 1
    for i in range(len(xs)-1):
        result[i+1] = result[i] + xs[i+1]
    return result

# Tests
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
assert derivative([1, 2, 3]) == [2, 6]
```

This script defines a function `derivative` which takes in a list of coefficients representing a polynomial and returns the coefficients of the derivative of this polynomial. The function employs a simple iteration approach, where each result is calculated from the previous one based on the polynomial rule. Initialized with `result[0] = 1` for the derivative of `x^0`, and then loops through the polynomial coefficients, each result is calculated by adding the adjacent coefficient to the `result` list.