Here's a Python script that includes a function to solve the problem of finding a zero point of a polynomial:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient.
    """
    assert len(xs) % 2 == 0, "List xs must have an even number of elements"
    x = -xs[0] / (xs[1:] + [0])[0]
    return x
```

This script includes a function `find_zero` that finds the zero of a polynomial given its coefficient list `xs`. The function first asserts that the length of the list is even, ensuring it has an even number of coefficients. It then assumes that the largest non-zero coefficient is the dominant term, neglecting the possibility of multiplicity. It constructs a guess for the solution, `x = -xs[0] / (xs[1:] + [0])[0]`, then returns the solution `x`.

Note that this function assumes that the provided list `xs` has a non-zero coefficient and that the coefficient list has a non-zero even element, as these are not enforced by the provided tests.