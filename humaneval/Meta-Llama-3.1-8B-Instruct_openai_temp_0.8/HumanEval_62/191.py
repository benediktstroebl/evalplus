Here's a Python function that implements the derivative of a polynomial.
```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of the polynomial, where xs[i] is the coefficient of the term x^i.

    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    if len(xs) == 1:  # Base case: derivative of constant term is 0
        return []
    return [i * x for i, x in enumerate(xs[1:], 1)]


# Example use cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([0, 1]))  # Output: [1]
print(derivative([0]))  # Output: []
```
This function calculates the derivative of a polynomial using the power rule of differentiation, which states that if we have a term of the form `x^i`, its derivative is `i * x^(i - 1)`. It uses a list comprehension to create the new list of coefficients, iterating over the input list `xs` starting from the second element (index 1) and multiplying each coefficient by its index (which represents the power to which `x` is raised). If the input list has only one element (which represents a constant term), the function returns an empty list, since the derivative of a constant is 0.