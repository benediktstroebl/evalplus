### Derivative of a Polynomial
#### Python Implementation
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: Derivative of the polynomial in the same form.
    """
    # Start with the second coefficient and increment by 1 for each higher coefficient
    return [xs[i] * i for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected: [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial and returns the coefficients of its derivative. The test cases demonstrate the function's usage and expected outputs.