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
    find_zero find x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    check for polynomial zero using even list with even number of coefficients and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

    """
   
    testing the test
    assert round(poly(xs=[1, 2]), 2) == round(find_zero([1, 2]), 2), "Poly and find_zero don't agree"
    assert round(poly(xs=[-6, 11, -6, 1]), 2) == round(find_zero([-6, 11, -6, 1]), 2), "Poly and find_zero don't agree"
    assert round(poly(xs=[1, 2, -3, -4]), 2) == round(find_zero([1, 2, -3, -4]), 2), "Poly and find_zero don't agree"
    assert round(poly(xs=[1, -1, 2, 3]), 2) == round(find_zero([1, -1, 2, 3]), 2), "Poly and find_zero don't agree"
    assert round(poly(xs=[-2, -3, 4, -5]), 2) == round(find_zero([-2, -3, 4, -5]), 2), "Poly and find_zero don't agree"
```
The function `poly` takes a list `xs` of coefficients of a polynomial and a number `x` as input and returns the polynomial evaluated at the given point `x`. The function uses the `math.pow()` function to evaluate the function to evaluate the polynomial at the given point `x`. The function then returns the sum of the product of each coefficient multiplied by the `math.pow()` function. The `find_zero` function is used to find the zero of a polynomial, which is the value of `x` that makes the polynomial equal to zero. 
The test cases use the `assert` function to check that the `poly` and `find_zero` functions are indeed evaluating the same values for the same input.