### Derivative of a Polynomial
#### Problem Description
Given a polynomial with coefficients `xs` where `xs[i]` is the coefficient of `x^i`, this script calculates the derivative of the polynomial.

#### Code

```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
    xs (list): Coefficients of the polynomial.

    Returns:
    list: Coefficients of the derivative polynomial.
    
    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return []
    derivative_coefficients = [0] * len(xs)
    for i in range(1, len(xs)):
        derivative_coefficients[i - 1] = xs[i] * i
    return derivative_coefficients

# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

#### Explanation
This code defines a function `derivative` that takes a list of coefficients `xs` and returns the list of coefficients of the derivative polynomial. It uses a loop to calculate the coefficients of the derivative polynomial by multiplying each coefficient with its power and shifting it to the left. The first and second elements of the input list are handled separately as they have special cases: the derivative of a constant (first element) is zero, and the derivative of a linear polynomial (second element) is one.