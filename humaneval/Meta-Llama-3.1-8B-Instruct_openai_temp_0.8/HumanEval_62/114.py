### Derivative of a Polynomial
#### Python Script

```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a given polynomial.
    
    Args:
    xs (list): A list of coefficients of a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    derivative_coeffs = []
    for i in range(1, len(xs)):
        # For each coefficient, multiply it by its exponent (i) and divide by the exponent (i) of the next lower degree term.
        # The exponent of the next lower degree term is i, hence the division by i.
        derivative_coeffs.append(xs[i] * i)
    return derivative_coeffs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

### Explanation

The function `derivative` calculates the derivative of a given polynomial by iterating over the coefficients of the polynomial, starting from the second coefficient (index 1). 

For each coefficient, it multiplies the coefficient by its exponent (`i`) and appends the result to the list of coefficients of the derivative of the polynomial. 

Finally, the function returns the list of coefficients of the derivative of the polynomial. 

Note that the derivative of `x^n` is `n*x^(n-1)`. Hence, in this code, we multiply each coefficient by its exponent and divide by the exponent of the next lower degree term, which is `i`.