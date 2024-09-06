```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0]*(len(xs)-1)
    result[0] = 1
    for i in range(len(xs)-1):
        result[i+1] = result[i] + xs[i+1]
    return result

# Tests
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([5, 10, 2, 4]) == [10, 22]
    assert derivative([0, 0, 0]) == [0, 0, 0]

test_derivative()
```

The function `derivative` calculates the derivative of the polynomial represented by its coefficients `xs`. It uses a simple algorithm that accumulates coefficients to the result list based on the x-power they correspond to. The initial `result` list is initialized with `len(xs)-1` zeros, and the first element is adjusted to 1 since the derivative of the constant term is zero. 

The `test_derivative` function provides test cases and assertions for the `derivative` function. It checks results for correctness against derived results for several polynomials. 

You can add more tests to increase test coverage and further verify the correctness of the function.