```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial (xs)(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return x
    max(xs) 
    """
    return math.floor(find_zero(xs))

# Test case:
xs = [1, 2]
result = poly(xs) # [2]
result = find_zero(xs) # 2
print("Poly Evaluation:", result)
```
The function `poly` calculates the polynomial with the coefficients passed as the argument. The function `find_zero` finds the zero of the polynomial passed to it, and the output is either the result of the `poly` function or the zero value, respectively.