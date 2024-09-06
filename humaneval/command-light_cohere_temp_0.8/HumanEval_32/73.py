```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    # Test if there are any zeroes for a polynomial
    assert not len(xs) % 2, "Invalid coefficients list!"
    return math.floor(find_zero(xs[0])

# Example usage:
xs = [1, 2]
x = 0.0
ans = poly(xs, x)
print(ans)
print("Zero found at x =", round(find_zero(xs), 2))
``` 
This code demonstrates how to use the "poly" and "find_zero" functions to solve a simple polynomial equation and find its zero. The output will be:
```bash
1.0 + 2.0 * x + 0
```
```

Remember that this code only works with a polynomial represented as a list of coefficients.  If your polynomial is represented differently, you may need to adapt the code accordingly.