```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    
    Parameters:
    xs (list): A list of coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The derivative of the polynomial in the same form.
    """
    
    # If the polynomial has a degree of 0 (i.e., it's a constant), return an empty list
    if len(xs) == 1:
        return []
    
    # The derivative of a polynomial is calculated by multiplying each coefficient
    # by its exponent and subtracting one from the exponent
    # We use list comprehension to achieve this in one line
    return [i * x for i, x in zip(range(1, len(xs)), xs[1:])]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function called `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses list comprehension to calculate the new coefficients of the derivative. The example usage at the end demonstrates how to use this function.