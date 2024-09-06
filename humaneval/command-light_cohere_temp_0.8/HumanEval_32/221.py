```python
import math

def find_zero(xs: list):
    """
    Check conditions for finding polynomial roots.
    Make sure there list has a list of coefficients xs for a polynomial.
    Check if list has even coefficients and number of coefficients is even.
    Check if largest coefficient is not zero.
    Check if the largest non-zero coefficient divides all other coefficients.
    Return None if no solution exists.
    """
   
    return x"
def poly(xs: list, x: float):
    """
    Evaluate polynomial with coefficients xs at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    """
    return find_zero([xs[0], xs[1], ...])

xs = [1, 2]
x = 2.0
result = poly(xs, x)
print("Result:", result)
result = find_zero(xs)
print("Find Zero Result:", result)
```
This code defines two functions: `poly` and `find_zero`. The `poly` function computes the value of a polynomial at a given point `x` by summing the product of each coefficient multiplied by the corresponding power. The `find_zero` function looks for the zeros of the polynomial and returns the corresponding values. Both functions are tested using the functions to evaluate the polynomial and find its roots, respectively.