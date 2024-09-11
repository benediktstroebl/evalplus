```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    
    Args:
    xs (list): A list of coefficients of a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: The derivative of the polynomial in the same form.
    """
    # If the polynomial is a constant, return an empty list
    if len(xs) == 1:
        return []
    
    # The derivative of a polynomial is calculated by multiplying each coefficient
    # by its exponent and then subtracting one from the exponent.
    # So, we use list comprehension to create a new list with these new coefficients.
    return [coeff * (deg - 1) for deg, coeff in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

This Python script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns the coefficients of its derivative. The script also includes two test cases to demonstrate its usage. The function uses list comprehension to calculate the derivative of the polynomial, creating a new list with the new coefficients. The `enumerate` function is used to get both the index and value from the `xs` list, simulating the effect of deg (degree) and coeff. 

The `start=1` parameter in the `enumerate` function is used to make the index start at 1 instead of 0, because the degree of a polynomial starts at 1 (not 0). The `coeff * (deg - 1)` expression calculates the new coefficients by multiplying the old coefficient by its old degree and then subtracting one from the old degree (to get the new degree). 

In the test cases, we pass the polynomial coefficients to the `derivative` function and print the result. The `derivative` function returns the coefficients of the derivative of the polynomial, which we can then use to represent the derivative.