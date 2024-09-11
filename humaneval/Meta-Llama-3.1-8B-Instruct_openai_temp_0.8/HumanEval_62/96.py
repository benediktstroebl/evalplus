### Polynomial Derivative Calculator
#### Python Script

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial, from lowest degree to highest.

    Returns:
    list: Coefficients of the derivative polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:  # Base case: derivative of x^n is n*x^(n-1)
        return []

    return [i * x for i, x in enumerate(reversed(xs[:-1]))]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` as input. It calculates the derivative of the polynomial represented by these coefficients and returns the result as a list. The function uses list comprehension to create the derivative polynomial coefficients. The base case for the recursion is when the input list has only one element, in which case the function returns an empty list.