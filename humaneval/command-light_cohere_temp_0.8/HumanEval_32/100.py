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
    find_zero finds x such that poly(x) = 0, returns only x, and passes tests that the list has even number of coefficients and the largest non-zero coefficient guarantees a solution.
    return round(math.floor(find_zero(xs)), 2)
```

The above Python script defines a function `poly` that evaluates a polynomial with given coefficients at a given point `x`. The function then returns the polynomial evaluated at `x`. 

The function `find_zero` finds the zeros of the polynomial. It does this by creating a list of coefficients of the polynomial and calling the `poly` function with that list. The function then finds the floor of the result and returns the result rounded to two decimal places. 

It then passes tests that the list has even number of coefficients and the largest non-zero coefficient guarantees a solution. 

Finally, the function returns the rounded result.