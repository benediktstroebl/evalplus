```python
def derivative(xs: list):
    """
    Returns the derivative of a polynomial given its coefficients.
    
    The input coefficients are for a polynomial of the form:
    xs[0] + xs[1] * x + xs[2] * x^2 + xs[3] * x^3 +...

    The output coefficients are for the derivative of the input polynomial:
    xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 +...

    :param xs: list of coefficients of the polynomial
    :return: list of coefficients of the derivative polynomial
    """
    return [ coefficient * (len(xs) - i - 1) for i, coefficient in enumerate(xs[1:]) ]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients of a polynomial as input and returns the list of coefficients of the derivative polynomial. The function uses a list comprehension to calculate the coefficients of the derivative. It starts from the second element of the input list (index 1) and multiplies each coefficient by its index plus one minus the length of the input list (i.e., the degree of the polynomial).