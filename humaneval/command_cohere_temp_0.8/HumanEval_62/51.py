```python
def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1j if i < n - 1 else 1    # imaginary number if not last iteration
        xs[i+1] *= 1j if i < n - 1 else 1  # imaginary number if not last iteration
    return result
```

The derivative of a polynomial is given by:
```
d / dx ( a_n x^n + a_(n-1) x^(n-1) + ... + a_1 x + a_0 ) = n * a_(n-1) x^(n-1) + ... + a_1
```

This is achieved by modifying the coefficients of the polynomial such that **every coefficient is multiplied by 1j (the imaginary unit) except the last one**, and the result is the derivative of the polynomial. The imaginary unit is chosen to avoid any division in the calculation and for convergence purposes.

The implementation follows the above method. It starts by initializing the result list with zeros and then iteratively multiplies the coefficients as described. The imaginary unit is introduced only for coefficients from the second to the last, both for the input and output. Thus, the output is the derivative of the polynomial, also in the form of coefficients.

The function utilizes reasonable Python practices, including type hints, docstrings, and testing through examples that reflect the function's behavior. It can be used as a standalone module to compute polynomial derivatives.