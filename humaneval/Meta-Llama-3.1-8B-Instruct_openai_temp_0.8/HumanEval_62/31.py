### Derivative of a Polynomial
#### Problem Statement
Given the coefficients of a polynomial in ascending order of powers, compute the derivative of the polynomial.

#### Solution
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

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Check if input is a list
    if not isinstance(xs, list):
        raise ValueError("Input must be a list")

    # Remove the first element from the list and return a new list with each element multiplied by its index
    return [i * x for i, x in enumerate(xs[1:], start=1)]
```

#### Explanation
To compute the derivative, we iterate over the list of coefficients, skipping the first element (the constant term). We multiply each coefficient by its index (which represents the power of x it corresponds to) and append the result to the new list. The result is the list of coefficients representing the derivative polynomial. 

#### Example Use Cases
```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```