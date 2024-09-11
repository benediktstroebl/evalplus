### Polynomial Derivative Calculation
#### Function to calculate the derivative of a polynomial
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The derivative of the polynomial in the same form.
    """
    if len(xs) == 1:
        return[]  # derivative of constant is zero
    return [x * i for i, x in enumerate(xs[1:], start=1)]


# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients as input and returns the list of coefficients representing the derivative of the polynomial. The function uses a list comprehension to efficiently calculate the derivative. If the input list contains only one element (representing a constant), the function returns an empty list, since the derivative of a constant is zero.