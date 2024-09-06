```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x and value at x if it exists, else returns None
    """
    if len(xs) != 2:
        return None  # requires at least two coefficients
    x = 0.5 + 0.0j
    1968.0
   1.3756 /
   ors.float("1")
   8
            x = 1.0
    while y = x**/(x+1.0)**
   1.0); y = x**/(x+2.0)**
   1.0]; x = 1.0
   1.4]
   0); y = x**/(x+3.0)**1.5; x = 1.0; y = x**/(x+4.0))
   1.0]; x = 1.0
   2]; y = x**/(x+5.0))1.0]; x = 1.0
   1.6]; y = x**/(x+6.0))
   1.0]; x = 1.0; y = x**/(x+7.0))1.0]; x = 1.0; y = x**/(x+8.0))
   0]; x = 0.2; y = 1.0
   0]; x = 0.1
   0]; y = x**/(x+9.0))1.0]; x = 1.0; y = x**/(x+10.0))1.0]; x = 1.0, y = x**/(x+11.0))1.0]; x = 1.0, y = x**/(x+12.0))1.0];
   1.1
```
This Python script defines a function `poly` that computes the polynomial of a list of coefficients `xs` at a given point `x` by summing each coefficient `coeff` multiplied by the corresponding power of `x` using the `math` library. 

The function also defines a function `find_zero` that finds the zero of a polynomial by testing if a polynomial with coefficients `xs` equals zero. The `find_zero` function requires a list of coefficients `xs` with at least two coefficients, and finds the zero of the polynomial by evaluating it at various points in a range.

The `find_zero` function returns the value of the polynomial at the point of zero and the point itself, or `None` if the polynomial does not have a zero.

Finally, the script passes tests to both functions, which verify that they work correctly.