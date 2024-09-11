```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): List of coefficients of the polynomial.

    Returns:
        list: List of coefficients of the derivative polynomial.
    """
    if len(xs) == 1:
        # Base case: derivative of a constant is 0
        return []
    
    derivative_coeffs = [i * xs[i] for i in range(1, len(xs))]
    return derivative_coeffs


# Test cases
print(derivative([3, 1, 2, 4, 5]))
# Output: [1, 4, 12, 20]

print(derivative([1, 2, 3]))
# Output: [2, 6]
```

This script uses list comprehension to create the derivative coefficients by multiplying each coefficient by its index `i`, starting from 1 (since the coefficient of the x term is the first term, not the x^0 term). The function returns an empty list if the input list has only one element (i.e., a constant).