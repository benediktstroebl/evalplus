```python
def derivative(xs: list):
    """
    Compute the derivative of a polynomial defined by the list of coefficients xs.

    Args:
        xs (list): List of coefficients of the polynomial. xs[i] is the coefficient of x^i.

    Returns:
        list: List of coefficients of the derivative polynomial.
    """
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return []
    else:
        # Initialize the derivative coefficients list with the coefficients of x^1 and all x^i with i > 1
        derivative_xs = [i * xs[i] for i in range(1, len(xs))]
        return derivative_xs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines the `derivative` function, which takes a list of polynomial coefficients `xs` and returns the coefficients of the derivative polynomial. It uses list comprehension to create the new coefficients list, where each coefficient is the product of the original coefficient and its corresponding exponent. The function handles the special cases where the input list is empty or has only one element, which correspond to the zero polynomial and the constant polynomial respectively. Finally, the script includes two test cases to demonstrate the function's behavior.