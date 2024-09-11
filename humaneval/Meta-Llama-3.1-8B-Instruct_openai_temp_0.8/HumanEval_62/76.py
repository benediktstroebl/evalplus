### Polynomial Derivative Calculator

#### Description
A Python script that calculates the derivative of a polynomial given its coefficients.

#### Code
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial.
                  xs[i] is the coefficient of x^i.

    Returns:
        list: Coefficients of the derivative polynomial.
              xs'[i] is the coefficient of x^(i-1).

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) == 1:
        return []  # Derivative of x^0 is 0

    return [i * x for i, x in enumerate(xs[1:], 1)]


# Example usage
if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))  # Output: [2, 6]
```

#### Explanation

1.  Check if the polynomial is constant (i.e., has only one term). If so, return an empty list, as the derivative of a constant is 0.
2.  Use a list comprehension to calculate the coefficients of the derivative polynomial. For each term x[i] \* x^(i-1), multiply the coefficient by the power (i-1) to get the coefficient of the derivative term.