```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
    xs (list): A list of coefficients representing a polynomial.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    if len(xs) == 1:  # Edge case: derivative of a constant is 0
        return []
    return [i * x for i, x in enumerate(xs[1:], 1)]


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses list comprehension to generate the coefficients of the derivative. If the input is a polynomial of degree 0 (i.e., a constant), the function returns an empty list, since the derivative of a constant is 0. The example usage shows how to use this function to calculate the derivatives of two polynomials.