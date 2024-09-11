### Derivative of Polynomial
#### Python Script
```markdown
### derivative.py

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * coeff for i, coeff in enumerate(xs[1:], 1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

### Explanation
This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to generate the coefficients of the derivative polynomial. The `enumerate` function is used to iterate over the coefficients starting from the second one (index 1), and the `i` variable represents the power of the term.

The script includes example usage of the `derivative` function and prints the results to the console.

### Running the Script
Save this script as `derivative.py` and run it using Python (e.g., `python derivative.py`). The output will be the coefficients of the derivative polynomials for the given examples.