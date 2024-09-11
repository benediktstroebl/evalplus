```markdown
### Derivative of a Polynomial

This script calculates the derivative of a polynomial given its coefficients.
#### Code

```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
        xs (list): Coefficients of the polynomial.
    
    Returns:
        list: Coefficients of the derivative polynomial.
    """
    derivative_xs = []
    for i in range(1, len(xs)):
        derivative_xs.append(i * xs[i])
    return derivative_xs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

#### Explanation

The `derivative` function iterates over the coefficients of the polynomial starting from the second coefficient (`i = 1`). For each coefficient, it multiplies it by its index (`i`) to get the corresponding coefficient of the derivative polynomial. Finally, it returns the list of coefficients of the derivative polynomial.

This implementation assumes that the input list of coefficients represents a polynomial of the form `a + bx + cx^2 + dx^3 +...`. The derivative of such a polynomial is given by `b + 2cx + 3dx^2 +...`. The index `i` in the loop corresponds to the exponent of `x` in the polynomial, and `i * xs[i]` gives the corresponding coefficient of the derivative polynomial.