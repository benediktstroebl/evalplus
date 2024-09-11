```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    The polynomial is represented as a list of coefficients, where the first coefficient (xs[0])
    is the constant term, the second coefficient (xs[1]) is the coefficient of x, the third
    coefficient (xs[2]) is the coefficient of x^2, and so on.

    Args:
        xs (list): A list of coefficients representing a polynomial.

    Returns:
        list: A list of coefficients representing the derivative of the input polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # If the polynomial has only one term (i.e., a constant), return an empty list.
    if len(xs) == 1:
        return []
    
    # Initialize an empty list to store the coefficients of the derivative.
    deriv = []
    
    # Iterate over the coefficients of the polynomial, starting from the second coefficient
    # (i.e., xs[1]) and ending at the second to last coefficient (i.e., xs[-2]).
    for i in range(1, len(xs) - 1):
        # The coefficient of the ith term in the derivative is i times the coefficient of the
        # (i+1)th term in the original polynomial.
        deriv.append(i * xs[i + 1])
    
    # If the polynomial has a degree greater than 1, the coefficient of the second to last
    # term in the derivative is the coefficient of the last term in the original polynomial.
    if len(xs) > 2:
        deriv.append(xs[-1])
    
    # Return the list of coefficients of the derivative.
    return deriv

# Test the function with some examples.
if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial represented as a list of coefficients. The example use cases are demonstrated in the code block using the `if __name__ == "__main__":` guard.