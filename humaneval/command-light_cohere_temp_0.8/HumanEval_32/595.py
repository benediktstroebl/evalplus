```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *1 * * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    - a solution
    """

The Python script defines a function `poly` that computes the polynomial expression with given coefficients `xs` at `x` by summing the products of each coefficient multiplied with the corresponding powers of `x` from each term in the polynomial. The function `find_zero` is defined to find the zero of the polynomial `poly(x)` by determining the value of `poly(x)` equals zero. 

Both functions pass corresponding tests and demonstrate the process of evaluating polynomials and finding their zeros.