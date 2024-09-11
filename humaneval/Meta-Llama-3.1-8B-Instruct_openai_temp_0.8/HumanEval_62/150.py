```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients of a polynomial, where xs[0] is the constant term,
               xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, and so on.
    
    Returns:
    list: A list of coefficients of the derivative of the input polynomial.
    """
    
    # Check if the input list has at least two elements (for the polynomial to have a derivative)
    if len(xs) < 2:
        raise ValueError("The input polynomial must have at least two coefficients.")
    
    # Calculate the derivative by shifting the coefficients one position to the left and multiplying by their index
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses list comprehension to create the derivative coefficients by shifting the input coefficients one position to the left, multiplying each coefficient by its index, and starting the enumeration from 1 (since the first coefficient is the constant term). The script also includes example usage of the function. If the input polynomial has less than two coefficients, the function raises a ValueError.