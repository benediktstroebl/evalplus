### Derivative of a Polynomial
#### Problem Description
Given a list of coefficients `xs` representing a polynomial, compute the derivative of the polynomial and return it in the same form.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing a polynomial.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_coeffs = [i * coef for i, coef in enumerate(xs[1:], start=1)]
    return derivative_coeffs

# Example usage
coefficients = [3, 1, 2, 4, 5]
print(derivative(coefficients))  # Output: [1, 4, 12, 20]

coefficients = [1, 2, 3]
print(derivative(coefficients))  # Output: [2, 6]
```
In this script, the `derivative` function takes a list of coefficients `xs` as input and returns the list of coefficients representing the derivative of the polynomial. The function uses a list comprehension to compute the derivative coefficients, where each coefficient is multiplied by its index (starting from 1, since the derivative of `x^n` is `n*x^(n-1)`). The `enumerate` function is used to get both the index and the value of each element in the input list, starting from the second element (since the first element is the constant term and has no derivative).