```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of the polynomial

    Returns:
        list: coefficients of the derivative polynomial
    """
    # The derivative of a polynomial is a new polynomial where each term's degree is reduced by one
    # For example, if we have 3 + 2*x + 4*x^2, the derivative is 2 + 8*x
    # So we start with the second term (index 1) and multiply it by its degree
    # Then we multiply each subsequent term by its degree and add it to the result
    if len(xs) == 1:
        return []
    result = [i * x for i, x in enumerate(xs[1:], 1)]
    return result

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([5]))  # Output: []
print(derivative([]))  # Output: []
```

This script defines a function `derivative` that calculates the derivative of a polynomial represented by its coefficients. It uses list comprehension to create a new list with the derivative coefficients. The function handles polynomials with one or more terms, and also handles the edge cases where the input polynomial is a constant or has no terms. The test cases at the end of the script demonstrate the function's behavior.