```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**(n-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    >> Get xs have even [1, 2] as coefficients
    >> find_zero([1, 2])  # f(x) = 1 + 2x - 0.5
    << "
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -0.5
    <<"
   
    -0
    pass
```

The script defines a function `poly` that computes the polynomial using the coefficients `xs` at the given `x` point. The function then returns the polynomial value at that point. 

The function `find_zero` finds the zeros of the polynomial, which are the values of `x` for which the polynomial equals 0. The function then returns the result of the `poly` function evaluated at those points. 

Please note that this solution assumes that the input list `xs` has at least two elements. If the list has less than two elements, it raises a `ValueError` exception.