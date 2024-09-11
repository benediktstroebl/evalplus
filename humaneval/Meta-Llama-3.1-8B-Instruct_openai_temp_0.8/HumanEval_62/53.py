### Derivative of a Polynomial
#### Python Script
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): Coefficients of a polynomial. xs[0] + xs[1] * x + xs[2] * x^2 +....

    Returns:
    list: Derivative of the polynomial in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # If the polynomial has only one term, return [0] at the same index
    if len(xs) == 1:
        return [0]
    
    # Remove the first coefficient (which is just a constant term)
    # All other coefficients are multiplied by their corresponding power + 1
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This Python script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns the coefficients of the polynomial's derivative. The function uses a list comprehension to calculate the derivative, multiplying each coefficient by its corresponding power plus one (starting from 1). If the polynomial has only one term, the function returns `[0]` at the same index. The script includes test cases to demonstrate the correctness of the `derivative` function.