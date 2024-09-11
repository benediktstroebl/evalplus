```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    The polynomial is represented as a list of coefficients from lowest to highest degree.
    For example, the polynomial 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4 would be represented as [3, 1, 2, 4, 5].
    
    Args:
        xs (list): A list of coefficients representing the polynomial.

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Use list comprehension to create the derivative coefficients
    # The derivative of x^n is n*x^(n-1)
    # So we multiply each coefficient by its degree (i.e., its index in the list)
    # and then subtract 1 from the degree
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses list comprehension to calculate the derivative coefficients. It assumes that the input list `xs` represents a polynomial with at least one term. The `enumerate` function is used to get both the index (the degree) and value of each element in the list `xs[1:]`, which represents the coefficients of the polynomial, excluding the constant term. The list comprehension then calculates the derivative coefficient for each term by multiplying the degree by the coefficient.