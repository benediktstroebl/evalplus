### Derivative of a Polynomial
#### Problem Description
Given a list of coefficients representing a polynomial, compute the derivative of the polynomial.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial.
        xs[0] + xs[1] * x + xs[2] * x^2 +...
    Returns:
    list: Coefficients of the derivative polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        # Base case: derivative of a constant is 0
        return []
    elif len(xs) == 2:
        # Base case: derivative of x^n is n*x^(n-1)
        return [xs[1]]
    else:
        # Derivative of a higher-degree polynomial
        return [x * i for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```
#### Explanation
The function uses list comprehension to compute the derivative of the polynomial. For each coefficient `x` at index `i`, the derivative is `x * i`. This is equivalent to the standard formula for the derivative of a polynomial, which is `n*x^(n-1)` for the term `x^n`.