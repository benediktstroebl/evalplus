```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented as a list of coefficients.

    Args:
    xs: A list of coefficients of a polynomial. xs[0] is the constant term,
    xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, and so on.

    Returns:
    A list of coefficients representing the derivative of the input polynomial.
    """
    # If the input polynomial is a constant (i.e., has only one term), the derivative is zero.
    if len(xs) == 1:
        return []
    
    # The derivative of a polynomial is found by differentiating each term and
    # multiplying the result by the power of x. Since we are given a list of coefficients,
    # we can use a list comprehension to efficiently compute the derivative.
    # The derivative of xs[i] * x^(i-1) is i * xs[i] * x^(i-2).
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([5]))  # []
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of that polynomial. The function uses a list comprehension to efficiently compute the derivative, and includes test cases to verify its correctness.