### Derivative of a Polynomial
#### Python Script

```markdown
### Code
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial, where xs[i] is the coefficient of x^i.

    Returns:
    list: Coefficients of the derivative polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_coefficients = [i * coefficient for i, coefficient in enumerate(xs[1:], 1)]
    return derivative_coefficients

### Example Usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

### Explanation
This script defines a function `derivative` that takes the coefficients of a polynomial as input and returns the coefficients of its derivative. The function uses a list comprehension to generate the coefficients of the derivative, where each coefficient is the product of its index `i` (starting from 1) and the corresponding coefficient from the input list.

Note that the function uses the `enumerate` function to iterate over the input list, starting from the second element (index 1) to calculate the coefficients of the derivative. The result is returned as a list.

The example usage at the end demonstrates how to use the `derivative` function to compute the coefficients of the derivative of two polynomials.