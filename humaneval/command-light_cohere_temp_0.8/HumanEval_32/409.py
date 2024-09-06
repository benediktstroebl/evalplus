```python
import math

def find_zero(xs):
    """
    > Find a zero of a polynomial represented as a list of coefficients xs
    >

    > If the list has an odd number of coefficients, return None.
    > Otherwise, find a zero of the polynomial represented by the list, using the "poly" function of the "math" module.
    """
    return poly(xs, 0.0)
```

def poly(xs: list, x: float):
    """
    > Evaluate polynomial with coefficients xs at point x
    >
    > Return the polynomial evaluated at x, using the "poly" function of the "math" module.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

xs = [1, 2]
x = 0.5

result = poly(xs, x)
print(result) # [0.0 + 0.10 * x + [
# => 0.15]

find_zero(xs) = [0.15]
print(find_zero(xs)) # [0.15]
```

The function "find_zero" returns the zero of the polynomial represented by the list of coefficients xs. The function "poly" returns the polynomial evaluated at the given point x.