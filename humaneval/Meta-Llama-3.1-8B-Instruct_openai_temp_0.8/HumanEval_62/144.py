Here's the Python script that solves the problem:

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
        list: Derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

#### Explanation

The `derivative` function takes a list of coefficients `xs` and returns the derivative of the polynomial. 

It uses a list comprehension to calculate the derivative. For each coefficient `x` in `xs[1:]` (i.e., all coefficients except the first one), it multiplies it by its index `i` (starting from 1) and adds it to the result list.

The example usage at the end demonstrates how to use the `derivative` function.
```