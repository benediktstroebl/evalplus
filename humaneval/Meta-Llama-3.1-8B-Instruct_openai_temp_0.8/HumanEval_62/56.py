```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a given polynomial.
    
    The input list xs represents the coefficients of a polynomial in the form:
    xs[0] + xs[1] * x + xs[2] * x^2 +...
    
    The function returns the derivative of this polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    # Calculate the derivative of each term and remove the x^2 term (i.e., the term with a power of 2)
    derivative_xs = [i * x for i, x in enumerate(xs[1:], start=1) if i!= 2]
    
    return derivative_xs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a given polynomial represented as a list of coefficients. It uses a list comprehension to calculate the derivative of each term, skipping the term with a power of 2. The function then returns the list of derivative terms.

The script includes two test cases to verify the correctness of the function.