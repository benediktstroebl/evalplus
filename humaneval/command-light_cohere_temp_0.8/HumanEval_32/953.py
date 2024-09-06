```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *poly, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that satisfies polynomial equation 0 = xs.poly
    find_zero returns only zero point, even if there are many solutions
    """
    # make sure xs has even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("must have even number of coefficients")

    # sort xs by magnitude
    xs.sort(key=lambda x: x[0])
    xs.sort()
    list(xs)

    # find x with a coefficient equal to zero
    for x in xs:
        if x[0] == 0:
            return x[1] * math.pow(x, x[1])  # return x value and squared value

    # all coefficients are zero
    return None
``` 
This code defines two functions, poly and find_zero. The function poly takes a list of coefficients and the value x as input and returns the polynomial evaluation at the given x. The function find_zero takes a list of coefficients as input and returns the x value that satisfies the polynomial equation 0 = xs. It first makes sure that the list has an even number of coefficients, then sorts the coefficients by magnitude. It then iterates through each coefficient equal to zero and returns the corresponding value. If no coefficients are zero, it returns None.