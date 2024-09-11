```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    The polynomial is represented as a list of coefficients, where the first element is 
    the coefficient of the constant term, and the element at index i is the coefficient 
    of the term with degree i. The derivative is calculated by multiplying each coefficient 
    by its term's degree and subtracting one from the degree.

    Args:
        xs (list): A list of coefficients representing the polynomial.

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
    """
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of the polynomial. The function uses a list comprehension to multiply each coefficient by its term's degree (which is its index in the list, starting from 1) and subtract one from the degree. The function is then tested with the provided examples.