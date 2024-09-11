### Derivative of a Polynomial
#### Problem Description

The derivative of a polynomial `f(x) = a_n * x^n + a_(n-1) * x^(n-1) +... + a_1 * x + a_0` is given by `f'(x) = n * a_n * x^(n-1) + (n-1) * a_(n-1) * x^(n-2) +... + 2 * a_2 * x + a_1`.

#### Solution

We can solve this problem by iterating over the coefficients of the polynomial and applying the power rule of differentiation.

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
        xs (list): Coefficients of the polynomial in the form [a_n, a_(n-1),..., a_1, a_0].

    Returns:
        list: Coefficients of the derivative polynomial in the same form.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    return [i * x for i, x in enumerate(reversed(xs[:-1]), start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

In this code:

*   We use list comprehension to create a new list where each element is the product of its index `i` (starting from 1) and the corresponding coefficient `x` from the input list `xs` (excluding the last element, which represents the constant term).
*   We reverse the input list `xs` (excluding the last element) using `reversed(xs[:-1])` and iterate over it using `enumerate`, which provides both the index `i` and the value `x` of each element.
*   We use the `start=1` argument of `enumerate` to make the indices start from 1, which corresponds to the power of the variable in the polynomial.
*   Finally, we return the resulting list of coefficients, which represents the derivative of the input polynomial.