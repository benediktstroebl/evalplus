```python
import math

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    def polynomial(x: float, xs: list):
        """
        Evaluates polynomial with coefficients xs at point x
        return xs.sum()
        polynomial returns the osc(x) = f(x) = 0
        """
    return polynomial(x, xs)

xs = [1, 2]

x = 0.5

f = find_zero(xs)

print("f(x) =", f(x))

```

In this Python script, the function find_zero returns the x-value where the polynomial f(x) equals zero. The function polynomial takes a coefficients of a polynomial and returns the value of the polynomial at the given point x.