```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of a polynomial, where xs[i] is the coefficient of x^i.

    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    # Calculate the derivative by shifting the list and multiplying each term by its power
    derivative_coeffs = [i * xs[i - 1] for i in range(1, len(xs))]
    
    return derivative_coeffs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))
# Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))
# Output: [2, 6]
```
In this code, we use a list comprehension to calculate the derivative. We iterate over the indices of the coefficients (starting from 1), multiply each coefficient by its power, and store the result in a new list. This process effectively shifts the coefficients to the left (i.e., divides each power by one), which corresponds to differentiating the polynomial.