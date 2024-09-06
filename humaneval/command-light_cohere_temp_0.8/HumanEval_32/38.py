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
    find_zero find x such that polynomial x = 0.
    find_zero returns only zero point, even if there are many.
    """
    most, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    return -1
   
    - # f(x) = 1 + 2x
    -0.5
    -0.03
   
    - # f(x) = -6 + 11x - 6x^2 + x^3
    -1.0
    -2.0
    - # f(x) = 1 + 2x
    -1.0
    -3.0

    - # f(x) = -6 + 11x - 6x^2 + x^3
    -1.0

    -1.0
    return - - minimum polynomial
    return


xs = [1, 2]
x = 0.5
result = poly(xs, x)
print(result)
result = find_zero(xs)
print(result)
``` 
The script defines a function `poly` that computes the value of a polynomial with a list of coefficients at a given point `x`. The function `find_zero` searches for the zero of a polynomial with a list of coefficients. 
Finally, the script prints the results.