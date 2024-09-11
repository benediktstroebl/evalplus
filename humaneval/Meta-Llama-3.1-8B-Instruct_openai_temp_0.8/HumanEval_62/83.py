### Derivative of a Polynomial
#### Problem Description

You are given a list of coefficients representing a polynomial and you need to find the derivative of this polynomial.

#### Solution
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
    xs (list): List of coefficients of the polynomial.

    Returns:
    list: List of coefficients of the derivative polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Check if input is a list
    if not isinstance(xs, list):
        raise TypeError("Input must be a list.")
    
    # Check if list is not empty
    if len(xs) == 0:
        raise ValueError("Input list must not be empty.")

    # The derivative of a constant term is 0, so we start from the second term.
    derivative_xs = [i * coeff for i, coeff in enumerate(xs[1:], start=1)]
    
    return derivative_xs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This function uses list comprehension to create a new list `derivative_xs` where each element is the product of its index `i` and the corresponding coefficient in the input list `xs`. The `enumerate` function is used to iterate over both the index and the value of each element in the list. The `start=1` argument is used to start the indexing from 1, not 0, since the first term of the polynomial is `xs[0]` and the first term of the derivative is `xs[1]`.