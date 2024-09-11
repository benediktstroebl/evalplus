### Derivative of a Polynomial
#### Problem Description
This script calculates the derivative of a polynomial given its coefficients.

#### Code
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....

    Return derivative of this polynomial in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

#### Explanation
This script uses a list comprehension to calculate the derivative of the polynomial.
- The `enumerate` function is used to iterate over the coefficients of the polynomial starting from the second coefficient (index 1).
- The `start=1` argument is used to make `enumerate` start counting from 1 (i.e., the power of the first term).
- The product of the power and the coefficient is calculated and returned as the derivative of the polynomial.

This solution has a time complexity of O(n), where n is the number of coefficients in the polynomial.