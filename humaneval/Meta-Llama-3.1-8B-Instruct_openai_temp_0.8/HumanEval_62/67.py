### Polynomial Derivative Calculator
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial.

    Parameters:
    xs (list): A list of coefficients representing a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    derivative_coefficients = [i * x for i, x in enumerate(xs[1:], start=1)]
    return derivative_coefficients

# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
In this script, we use a list comprehension to calculate the derivative of the polynomial. The derivative of `xs[i] * x^i` is `i * xs[i] * x^(i-1)`. We use the `enumerate` function to get both the index `i` and the value `x` of each coefficient in `xs`. The `start=1` argument tells `enumerate` to start counting from 1 instead of 0.