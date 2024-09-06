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
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x - 0.5
    # first test
   
    if len(xs) != 2:
        raise ValueError("Invalid coefficients list")
    return xs[0]
```  # last coefficient is always 1