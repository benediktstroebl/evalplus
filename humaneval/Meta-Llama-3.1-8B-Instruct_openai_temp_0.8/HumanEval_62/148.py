### Derivative of a Polynomial
#### Python Function to Calculate Derivative of a Polynomial

Here's a Python function that takes coefficients of a polynomial as input and returns its derivative in the same form.

```python
def derivative(xs: list) -> list:
    """
    Returns derivative of the polynomial represented by coefficients in xs.
    
    The polynomial is in the form: xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    :param xs: list of coefficients of the polynomial
    :return: list of coefficients of the derivative polynomial
    """
    if len(xs) <= 1:
        return []
    
    # The derivative of a constant is 0
    # The derivative of x^n is n*x^(n-1)
    derivative_coefficients = [i * coefficient for i, coefficient in enumerate(xs[1:], start=1)]
    
    return derivative_coefficients

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This function uses a list comprehension to generate the coefficients of the derivative polynomial. It starts from the second coefficient (`xs[1]`) and multiplies each coefficient by its index (`i`) to calculate the coefficients of the derivative. If the input list has one or zero elements, it returns an empty list because the derivative of a constant is zero.