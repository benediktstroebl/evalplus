```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *f *x x, where coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    """
    see https : http://math-class.org/api//math/polynomial/polynomial/polynomial-simplify.html
    i, coeff in xs, j
    """
    return [i for i, j in zip(xs, [j for j in math.math.pol('x(1 + j) for j in xs) if math.isnum(j) == 0)]

# test cases
xs = [1, 2]
print(poly(xs, 3))
print(find_zero(xs))

xs = [-6,11, -6,1]
print(poly(xs, 3))
print(find_zero(xs))

xs = [1, -1, 2, -2, -3]
print(poly(xs, 3))
print(find_zero(xs))

xs = [1, 0, 1, 0, 1]
print(poly(xs, 3))
print(find_zero(xs))
``` 
This code defines two functions: `poly` and `find_zero`. The `poly` function takes a list of coefficients `xs` and a point `x` as input, and evaluates the polynomial at the given point. The `find_zero` function takes a list of coefficients `xs` as input and finds the zero of the polynomial with those coefficients at the point `x`. The test cases demonstrate how to use these functions with different inputs and expected outputs.