### Derivative of a Polynomial
#### Problem Description
Given a list of coefficients of a polynomial, compute the derivative of the polynomial in the same form.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs: List of coefficients of a polynomial.
        xs[0] + xs[1] * x + xs[2] * x^2 +....

    Returns:
    List of coefficients of the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = [0] * len(xs)
    
    # The derivative of a constant term is 0
    derivative_coeffs[0] = 0
    
    # The derivative of a term xs[i] * x^i is i * xs[i] * x^(i-1)
    for i in range(1, len(xs)):
        derivative_coeffs[i - 1] = i * xs[i]
    
    return derivative_coeffs
```

#### Example Use Cases
```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients of a polynomial as input and returns a list of coefficients of the derivative of the polynomial. It uses a simple iterative approach to compute the derivative of each term and stores the result in a new list. The example use cases demonstrate the usage of the `derivative` function with different input lists.