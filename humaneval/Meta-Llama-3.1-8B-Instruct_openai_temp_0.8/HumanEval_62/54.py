### Derivative of a Polynomial
#### Problem Description
Given the coefficients of a polynomial in the form `xs[0] + xs[1] * x + xs[2] * x^2 +...`, 
compute the derivative of this polynomial and return it in the same form.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial.
            xs[0] is the constant term, xs[1] is the coefficient of x,...
            xs[n] is the coefficient of x^(n-1).

    Returns:
        list: Coefficients of the derivative polynomial.
            xs[0] is the constant term, xs[1] is the coefficient of x,...
            xs[n-1] is the coefficient of x^(n-1).
    """
    # If the polynomial is of degree 0 (constant), return an empty list
    if len(xs) == 1:
        return []
    # Otherwise, compute the derivative coefficients using the power rule
    else:
        return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```