### Derivative of a Polynomial
#### Problem Description

Given the coefficients of a polynomial in ascending order of powers, calculate its derivative.

#### Solution

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in ascending order of powers.

    Returns:
        list: Derivative of the polynomial, in the same form.
    """
    # Use list comprehension to apply the power rule of differentiation
    # The power rule states that if f(x) = x^n, then f'(x) = n*x^(n-1)
    # For our coefficients, this translates to multiplying by the power of x (i.e., the index of the coefficient) and decreasing the power by 1
    return [i * coef for i, coef in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This solution uses Python's list comprehension feature to apply the power rule of differentiation to each coefficient, incrementing the power (i.e., the index) and multiplying by the original coefficient. The `enumerate` function is used to get both the index and value of each element in the input list, with `start=1` to make the indices start at 1 (since the power of x is 1 for the constant term).