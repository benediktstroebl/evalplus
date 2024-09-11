### Derivative of a Polynomial
#### Python Function to Calculate Derivative

```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial.

    The polynomial is represented by a list of coefficients, where
    xs[0] + xs[1] * x + xs[2] * x^2 +... is the polynomial.

    Args:
        xs (list): List of coefficients of the polynomial.

    Returns:
        list: List of coefficients of the derivative of the polynomial.
    """
    if len(xs) == 1:  # Handle the case when xs has only one element
        return []
    elif len(xs) == 0:  # Handle the case when xs is empty
        return None
    else:
        return [i * xs[i] for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

In this code, we use a list comprehension to calculate the derivative of the polynomial. The derivative of `xs[i] * x^i` is `i * xs[i] * x^(i-1)`, so we multiply each coefficient by its index (starting from 1) to get the coefficients of the derivative. If the input list `xs` has only one element or is empty, we return a special value (`[]` or `None`) to indicate this.