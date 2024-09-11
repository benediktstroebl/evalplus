Here is a Python script that defines a function to calculate the derivative of a polynomial represented as a list of coefficients.

```markdown
### Derivative of a Polynomial
#### Problem Statement
Calculate the derivative of a polynomial represented as a list of coefficients.

#### Solution

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
    # Trim the list by removing the first coefficient (the constant term)
    # because the derivative of a constant is 0
    return [i * coeff for i, coeff in enumerate(xs[1:], 1)]
```

#### Example Usage

```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Output: [2, 6]
```

#### Explanation
The derivative of a polynomial `xs[0] + xs[1] * x + xs[2] * x^2 +...` is `xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 +...`. This can be implemented using a list comprehension, where each coefficient `xs[i]` is multiplied by its index `i` (starting from 1, because the derivative of the constant term is 0). The `enumerate` function is used to get both the index and the value of each element in the list.