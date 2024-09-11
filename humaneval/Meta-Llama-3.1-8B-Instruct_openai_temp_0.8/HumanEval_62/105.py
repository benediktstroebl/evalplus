```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
        xs (list): A list of coefficients representing the polynomial.
            The first element is the constant term, and each subsequent element is the coefficient of the next highest power of x.
    
    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
    """
    if len(xs) == 1:  # Handle the case where the polynomial is just a constant
        return [0]
    
    # Use list comprehension to calculate the derivative of each term
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of the polynomial. It uses list comprehension to efficiently calculate the derivative of each term. The `enumerate` function is used to get both the index and value of each element in the list. The `if len(xs) == 1` check is added to handle the case where the polynomial is just a constant, in which case the derivative is 0.