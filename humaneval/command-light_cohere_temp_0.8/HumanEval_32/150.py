```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """ >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -1.0
   
    -0.0
    20
   it is a polynomial of degree n with real coefficients, so it has n+1 coefficients, xs=[xs[0], xs[1], ..., xs[n]]. Each coefficient is a real number, so it can be represented as an float, and x is also a float.

So, to evaluate a polynomial, we simply return the sum of the product of each coefficient multiplied by the corresponding term of the polynomial evaluated at x.

To find the zero of a polynomial, we set the polynomial equal to 0 and then solve for x. The solution to this equation will be the value of x that makes the polynomial equal to 0.

Finally, we test our functions with the following code:
```python
import math

xs = [1, 2]
print("poly:", poly(xs,1)) # f(x) = 1 + 2x
-0.5

xs = [1, -6, 11, -6, 1]
print("find_zero:", find_zero(xs)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
1.0

xs = [-6, 11, -6, 1]
print("find_zero:", find_zero(xs)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
-1.0
```