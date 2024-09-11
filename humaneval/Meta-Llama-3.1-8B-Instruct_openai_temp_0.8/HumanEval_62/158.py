```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
        xs (list): A list of coefficients of a polynomial.
                  xs[0] is the constant term, xs[1] is the coefficient of x, 
                  xs[2] is the coefficient of x^2, and so on.

    Returns:
        list: A list of coefficients of the derivative of the input polynomial.
    """

    # If the input list has only one element, return an empty list
    if len(xs) == 1:
        return []

    # Initialize an empty list to store the coefficients of the derivative
    derivative_xs = []

    # For each coefficient in the input list, starting from the second one (index 1)
    for i in range(1, len(xs)):
        # Multiply the coefficient by its index and append it to the derivative_xs list
        derivative_xs.append(i * xs[i])

    # Return the list of coefficients of the derivative
    return derivative_xs


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([5]))  # Expected output: []
print(derivative([]))  # Expected output: []
```