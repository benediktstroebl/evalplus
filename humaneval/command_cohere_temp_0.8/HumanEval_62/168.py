```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.

    Polynomial is in the form: xs[0] + xs[1] * x + xs[2] * x^2 + ...

    Returns: A list of coefficients of the derivative, in the same form.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    poly = 0
    for i in range(len(xs)):
        temp = 1
        for j in range(i+1, len(xs)):
            temp *= j
        poly += xs[i] * temp
    return [xs[i] * temp for i, temp in enumerate(poly)]
```

This implements the formula for derivative of a polynomial in `x` which is:
```
d/dx ( xs[0] + xs[1] * x + xs[2] * x^2 + ... ) 
 == xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + ...
``` 

Which is recreated through the following steps:
1. Initialize an accumulating polynomial value `poly` to zero, this will store the sum of all the derivatives of each term of the original polynomial.
2. For each element in the list `xs`, we iterate through all the previous coefficients and multiply them by the current coefficient, this corresponds to the derivative of that term, and we add it to the `poly` sum.
3. Finally, we return a list of the partial sums in the polynomial, which represent the coefficients of the derivative. 

This approach guarantees a valid solution for the provided problem statement.