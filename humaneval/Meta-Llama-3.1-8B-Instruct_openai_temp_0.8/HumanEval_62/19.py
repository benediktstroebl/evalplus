### Derivative of a Polynomial
#### A Python Function to Calculate the Derivative of a Polynomial
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The coefficients of the derivative polynomial
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []

    # Start from the second coefficient (index 1) and iterate over the rest
    for i in range(1, len(xs)):
        # The derivative of xs[i] * x^(i-1) is i * xs[i] * x^(i-2)
        # So we multiply the current coefficient by the current power of x
        derivative_coeffs.append(i * xs[i])

    # Return the coefficients of the derivative polynomial
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Expected output: [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial and returns the coefficients of the derivative polynomial. The function uses a simple loop to calculate the derivative of each term in the polynomial. The time complexity of this function is O(n), where n is the number of terms in the polynomial.