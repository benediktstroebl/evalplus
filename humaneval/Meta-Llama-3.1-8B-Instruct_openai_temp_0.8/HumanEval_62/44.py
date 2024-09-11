### Derivative of a Polynomial
#### Problem Description
Given a list of coefficients representing a polynomial, compute the derivative of the polynomial in the same form.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial, where xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: Derivative of the polynomial in the same form.
    """
    # The derivative of x^n is n * x^(n-1)
    # So, we multiply each coefficient by its index (except the first one)
    # and remove the first element (the constant term) from the list
    return [i * xs[i] for i in range(1, len(xs))]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```
This solution uses a list comprehension to create the derivative of the polynomial. It multiplies each coefficient by its index (except the first one), which corresponds to the power of x in the polynomial, and removes the first element (the constant term). The result is the derivative of the polynomial in the same form.