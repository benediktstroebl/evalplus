### Calculating the Derivative of a Polynomial
#### Overview
The following Python script defines a function `derivative` that calculates the derivative of a given polynomial, represented by its coefficients.

#### Code
```markdown
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients, where xs[0] is the coefficient of x^0,
               xs[1] is the coefficient of x^1, and so on.

    Returns:
    list: A list of coefficients representing the derivative of the input polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a polynomial is the coefficient of x^n times n*x^(n-1)
    # Therefore, we can calculate the derivative by multiplying each coefficient
    # by its index and removing the first element (coefficient of x^0)
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script uses list comprehension to efficiently calculate the derivative of the polynomial. The `enumerate` function is used to get both the index and value of each element in the list, and the `slice` notation `xs[1:]` is used to exclude the first element (coefficient of x^0).