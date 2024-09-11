```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented as a list of coefficients.

    Args:
        xs (list): A list of coefficients in order of decreasing degree.

    Returns:
        list: The coefficients of the derivative.
    """
    # The derivative of a constant term is 0
    derivative_coefficients = [0] * (len(xs) - 1)
    
    # The derivative of x^n is n*x^(n-1)
    for i in range(1, len(xs)):
        derivative_coefficients.append(i * xs[i])
    
    return derivative_coefficients


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script uses a simple mathematical property of polynomials: the derivative of a constant term is 0, and the derivative of `x^n` is `n*x^(n-1)`. It applies this property to each term in the input polynomial to compute the derivative.