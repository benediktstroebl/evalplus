```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    :param xs: list of coefficients
    :return: list of coefficients of the derivative polynomial
    """
    if len(xs) < 2:
        # If the input polynomial is a constant, its derivative is zero.
        return []
    elif len(xs) == 2:
        # If the input polynomial is linear, its derivative is its coefficient.
        return xs[:-1]
    else:
        # For higher degree polynomials, the derivative of the ith term is i(xs[i]).
        return [i * x for i, x in enumerate(xs[1:], start=1)]


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This Python script defines a function `derivative` that calculates the derivative of a polynomial represented as a list of coefficients. The function iterates over the coefficients, starting from the second one, and multiplies each coefficient by its index to obtain the corresponding coefficient in the derivative polynomial. If the input polynomial is a constant or linear, the function returns an empty list or the coefficient itself, respectively. The example usage demonstrates how to call the `derivative` function with different inputs.