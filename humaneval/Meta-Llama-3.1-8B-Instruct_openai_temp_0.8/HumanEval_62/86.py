### Polynomial Derivative Calculator
#### Problem Description
This Python script calculates the derivative of a given polynomial represented as a list of coefficients.

#### Code
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial represented as a list of coefficients.
    
    Args:
        xs (list): List of coefficients [a, b, c, d,...] representing the polynomial:
            a + b*x + c*x^2 + d*x^3 +...
    
    Returns:
        list: List of coefficients [b, 2c, 3d, 4e,...] representing the derivative of the polynomial.
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example use cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
#### Explanation
This script uses list comprehension to calculate the derivative of the polynomial. The `enumerate` function is used to iterate over the coefficients starting from the second one (index 1), and multiplying each coefficient by its index (which represents the power of x). The `start` parameter of `enumerate` is set to 1 to start the indexing from 1.