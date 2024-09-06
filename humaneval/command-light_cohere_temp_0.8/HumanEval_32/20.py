```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0
    find_zero returns only zero point, even if there are many.
    There, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   -0.5
   
   
    first, biggest polynomial factor
    """
    i = 0
    while i < len(xs)-1:
        if xs[i] != 0:
            break
        i += 1

    # choose any root
    root = math.sqrt(xs[i])
    # take square root
    roots = [root, root**2]

    # return roots

xs = [1, 2]
print(find_zero(xs))  # f(x) = 1 + 2x - 0.5
```