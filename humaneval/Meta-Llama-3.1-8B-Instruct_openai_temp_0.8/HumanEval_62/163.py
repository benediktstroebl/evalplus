### Derivative of a Polynomial

#### Problem Description
Given a list of coefficients `xs` representing a polynomial `xs[0] + xs[1] * x + xs[2] * x^2 +...`, return the derivative of this polynomial in the same form.

#### Solution
```python
def derivative(xs: list):
    """
    Derivative of a polynomial.

    Args:
        xs (list): Coefficients of a polynomial.

    Returns:
        list: Derivative of the polynomial in the same form.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) <= 1:
        return []
    return [i * xs[i] for i in range(1, len(xs))]
```
#### Explanation
The derivative of a polynomial is calculated by multiplying each term's coefficient by its exponent and subtracting one from the exponent. This can be achieved using a list comprehension. The code iterates over the coefficients starting from the second term (index 1) because the first term has no derivative. The product of the exponent and the coefficient is then added to the result list.

#### Example Use Cases
```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([5]))  # Output: []
print(derivative([9]))  # Output: []
print(derivative([]))  # Output: []
```