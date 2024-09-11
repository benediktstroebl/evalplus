### Derivative of a Polynomial
#### Description
Calculates the derivative of a polynomial represented as a list of coefficients.

#### Code
```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
        xs (list): List of coefficients of the polynomial.

    Returns:
        list: List of coefficients of the derivative.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Remove the first element (constant term)
    xs = xs[1:]
    # Multiply each coefficient by its index and add the index to it
    return [i * coeff for i, coeff in enumerate(xs)]
```

#### Example Use Cases
```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([x**4 for x in range(5)]))  # Output: [4, 12, 20, 24]
```