### Derivative of a Polynomial
#### Code
```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        # Base case: derivative of a constant is 0
        return []
    else:
        # Apply power rule for differentiation
        return [i * xs[i] for i in range(1, len(xs))]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

#### Explanation
The `derivative` function takes a list of coefficients `xs` representing a polynomial and returns the coefficients of its derivative.

For a polynomial `xs[0] + xs[1] * x + xs[2] * x^2 +...`, the derivative is obtained by applying the power rule, which states that the derivative of `x^n` is `n * x^(n-1)`.

In the code, the base case is when the input list `xs` has only one element, which represents a constant polynomial. In this case, the derivative is zero, and an empty list is returned.

For the general case, the derivative is computed using a list comprehension that multiplies each coefficient `xs[i]` by its power `i` and returns the resulting list of coefficients. The `range(1, len(xs))` ensures that we only consider the coefficients of the polynomial, excluding the constant term.