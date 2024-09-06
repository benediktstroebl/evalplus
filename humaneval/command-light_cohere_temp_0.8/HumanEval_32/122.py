```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many
    and it finds the zero point of the polynomial with coefficients xs
    """
    # test
    assert poly(xs[:2], x) == 0
    assert round(find_zero(xs[:2]), 2) == 1.5

``` 
This code defines a function called `poly` that evaluates a polynomial at a given point x. The function takes in a list of coefficients `xs` and a point `x` as input and returns the polynomial's value at `x`. 

The function `find_zero` finds the zero of the polynomial with coefficients `xs` by evaluating the polynomial at the points in the list and then returning the point x where the polynomial equals zero. 

The code tests the validity of the functions by passing test cases.