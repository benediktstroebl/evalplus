```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial(xs, x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    guaranteed.
    # largest number of coefficients because
    # ...
    # The coefficient with the largest absolute value is the leading coefficient
    # sort coefficients in descending order and take the first one
    # the remaining coefficients are multiplied by the product of the leading coefficient
    # and the power of the largest coefficient value
    # so the largest absolute value of a coefficient remains the same and the power of
    # the largest coefficient value increases by one for each coefficient
    # which guarantees the largest absolute value of a coefficient will be multiplied by all the coefficients
    # and the largest coefficient value multiplied by the largest coefficient value will be the largest number in the polynomial
    # and the polynomial equation will be guaranteed to have the largest number as its root
    # so the polynomial equation has the largest number as its root and satisfies the condition of having the largest number as its root.
    # largest number of coefficients is the same as the leading coefficient
    # take the product of the largest coefficient value and all the coefficients and the power of the largest coefficient value and subtract the product from the polynomial
    # and repeat the process until the product of the largest coefficient value and all the coefficients and the power of the largest coefficient value is smaller than the specified threshold
    # and repeat the process until the product of the largest coefficient value and all the coefficients and the power of the largest coefficient value is equal to zero
    # and the largest number of the polynomial equation has been subtracted from the polynomial equation
    # so the largest number of the polynomial equation has been subtracted from the polynomial equation and the polynomial equation is equal to the number
    # and the largest number of the polynomial equation is its root
    """

xs = [1, 2]
x = 1.0
poly(xs, x)
find_zero(xs)
```