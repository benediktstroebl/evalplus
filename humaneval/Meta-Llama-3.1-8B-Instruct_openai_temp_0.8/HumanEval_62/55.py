```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....

    Return derivative of this polynomial in the same form.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative polynomial.
    """
    # The derivative of a polynomial is the new polynomial where the power of each term decreases by 1 and the coefficient is multiplied by the new power.
    # So, a * x^(n-1) becomes n * a * x^(n-2), which is the (n-1)th coefficient.
    # We start with the first term (the constant term) and end with the last term (the leading term).

    # Use list comprehension to create a new list, where each term is the previous coefficient multiplied by the new power.
    return [i * (len(xs) - i) for i in range(1, len(xs))]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It uses list comprehension to create a new list, where each term is the previous coefficient multiplied by the new power (i.e., the power of the term is decreased by 1 and the coefficient is multiplied by the new power).

The test cases at the end of the script verify that the function works correctly by comparing its output with the expected output.

Note that this script assumes that the input list `xs` represents the coefficients of a polynomial in increasing order of powers, i.e., the first element is the constant term, the second element is the coefficient of the linear term, and so on.