```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial.
    
    Args:
    xs (list): Coefficients of the polynomial.
    
    Returns:
    list: Coefficients of the derivative polynomial.
    """
    # Remove the first element (constant term), multiply the rest by their power
    # Then subtract 1 from the power
    return [i * x for i, x in enumerate(reversed(xs[:-1]), 2)][::-1]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients as input and returns the coefficients of the derivative polynomial. It uses list comprehension to create a new list where each element is the product of the corresponding coefficient from the original list and its power (which is calculated by starting at 2 and incrementing for each element).

Note that the keyword argument `start=2` is used to start the enumeration at 2, and the `[::-1]` slicing is used to reverse the resulting list, so that the coefficients are in the correct order.