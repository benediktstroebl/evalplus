```python
def derivative(xs: list):
    """
    Derivative of a polynomial represented by coefficients of the polynomial.
    
    Args:
        xs (list): A list of coefficients, where xs[i] is the coefficient of x^i.
    
    Returns:
        list: A list of coefficients of the derivative polynomial.
    
    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Check if the input is a list
    if not isinstance(xs, list):
        raise TypeError("Input must be a list")
    
    # Remove any leading zeros from the list
    while len(xs) > 1 and xs[-1] == 0:
        xs.pop()
    
    # If the list has only one element, return an empty list
    if len(xs) == 1:
        return []
    
    # Calculate the derivative of the polynomial
    derivative_xs = [i * xs[i] for i in range(1, len(xs))]
    
    return derivative_xs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines the function `derivative(xs)` that takes a list of coefficients `xs` representing a polynomial and returns a list of coefficients representing the derivative of that polynomial. It uses a list comprehension to calculate the derivative, where each element `i` of the coefficients list is multiplied by `i` to obtain the corresponding element in the derivative coefficients list.