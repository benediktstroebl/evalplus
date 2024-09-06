Here's a Python script that includes a function to solve the problem of finding a zero point of a polynomial:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check for once whether xs has even length and handle erroneous cases
    if len(xs) % 2 == 1 or max(xs) == 0:
        return "erroneous case"

    # partition xs into tow halves
    xs1, xs2 = xs[:len(xs) // 2], xs[len(xs) // 2:]

    # find zeros in xs1
    x1 = find_zero_inner(xs1)
    if x1 == "erroneous case":
        return "erroneous case"

    # find zeros in xs2
    x2 = find_zero_inner(xs2)
    if x2 == "erroneous case":
        return "erroneous case"

    # find intersection zeros
    while True:
        x = (x1 + x2) / 2
        if x1 == x2:
            return x
        elif poly(x, x1) <= 0:
            x2 = x
        else:
            x1 = x

def find_zero_inner(xs: list) -> float:
    """
   recursive helper function to find_zero
    """
    # Handle case of erroneous input (all coefficients are zero)
    if min(xs) < 0:
        return "erroneous case"
    # Handle case of polynomial with only one coefficient
    if len(xs) == 1:
        return 0
    else:
        # partition xs into two halves
        mid = len(xs) // 2
        xs1, xs2 = xs[:mid], xs[mid:]
        # find zeros in xs1
        x1 = find_zero_inner(xs1)
        if x1 == "erroneous case":
            return "erroneous case"
        # find zeros in xs2
        x2 = find_zero_inner(xs2)
        if x2 == "erroneous case":
            return "erroneous case"
        # find intersection zeros
        while True:
            x = (x1 + x2) / 2
            if x1 == x2:
                return x
            elif poly(x, x1) <= 0:
                x2 = x
            else:
                x1 = x
```

This code includes two main functions 'poly' and `find_zero`. The `poly` function evaluates the polynomial of coefficients `xs` at point `x` and returns it. The `find_zero` function returns the point `x` such that `poly(x) = 0`. It only returns one zero point, even if there are many. It also only takes a list `xs` with an even number of coefficients and the largest non-zero coefficient as it guarantees a solution. The function uses a recursive approach and handles