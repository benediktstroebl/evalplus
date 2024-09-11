### Derivative of a Polynomial
#### Problem Description
Given the coefficients of a polynomial in the form of a list, this script will calculate and return the derivative of the polynomial in the same form.

#### Solution
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of the constant term is 0
    derivative_coefficients = []
    
    # The derivative of the linear term is the coefficient
    # The derivative of the quadratic term is 2 times the coefficient
    # In general, the derivative of the nth term is n times the coefficient
    for i in range(1, len(xs)):
        derivative_coefficients.append(i * xs[i])
    
    return derivative_coefficients
```

#### Example Use Cases
```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses a simple loop to iterate over the coefficients of the polynomial, ignoring the constant term (which has no effect on the derivative). For each coefficient, it calculates the corresponding coefficient of the derivative using the rules for polynomial differentiation, and appends it to the list of derivative coefficients. The final list of derivative coefficients is then returned.