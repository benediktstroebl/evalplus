### Derivative of a Polynomial
#### A Python Function to Calculate the Derivative of a Polynomial

In this script, we will create a function `derivative` that takes a list of coefficients as input and returns the coefficients of the derivative of the polynomial represented by those coefficients.

```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): A list of coefficients representing a polynomial.

    Returns:
        list: The coefficients of the derivative of the polynomial.
    """
    # Initialize an empty list to store the derivative coefficients
    derivative_coeffs = []
    
    # Iterate over the coefficients of the polynomial, starting from the second one (index 1)
    for i in range(1, len(xs)):
        # The derivative of a coefficient is the coefficient times its index
        derivative_coeffs.append(xs[i] * i)
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients as input and returns the coefficients of the derivative of the polynomial. The function uses a loop to iterate over the coefficients, starting from the second one (index 1) and calculates the derivative of each coefficient by multiplying it with its index. The resulting derivative coefficients are stored in a new list, which is then returned by the function. The script also includes test cases to demonstrate the function's correctness.