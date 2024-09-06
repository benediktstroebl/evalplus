```python
import math
def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("Input must be a list of coefficients of a polynomial with exactly 2 elements")
    return math.pow(xs[0], 0) ** xs[1]
```
The function find_zero receives a list xs which are coefficients of a polynomial, and returns the value of the zero of the polynomial x, it only takes lists with two coefficients, even if there is more coefficients, it returns a ValueError, so it is necessary to pass lists with one or more coefficients to find the zero of the polynomial.