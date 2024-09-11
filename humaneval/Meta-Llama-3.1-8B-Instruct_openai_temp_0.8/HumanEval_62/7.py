### Derivative of a Polynomial
#### Python Script
```markdown
### derivative.py
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial, where xs[i] is the coefficient 
               of x^i.

    Returns:
    list: Coefficients of the derivative polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]


if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
    print(derivative([1, 2, 3]))  # [2, 6]
```
#### Explanation

The `derivative` function calculates the coefficients of the derivative of a polynomial given its coefficients. It uses a list comprehension to iterate over the coefficients and their indices, starting from 1 (since the first coefficient is the constant term and does not contribute to the derivative). The derivative of each term `xs[i] * x^i` is `i * xs[i] * x^(i-1)`, which corresponds to the coefficient at index `i` in the derivative polynomial.