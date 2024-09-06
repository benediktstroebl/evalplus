```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes the polynomial equal to 0
    find_zero returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    """
    # By adding one to each x in xs, we can always make the polynomial equal to 0
    ?>> round(find_zero([1, 2])) # f(x) = 1 + 2x
    -0.5
    also works.
    """, because any polynomial over all numbers of zeros. 
    
    # Because testing polynomial of degrees 4, 6, 8, 10, 12, 13, 14, 15 over x
    -0.5
    -0.05
    also works.
    # The fact of degree 14 
    -0.039999999999
    if a polynomial has degree n>=14, then testing over all numbers is not efficient.
    ```