```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * *math.pow(xi) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x and it only returns the first solution, even if there are many solutions
    """
    x1 = -math.pow(x, len(xs)) / math.pow(max(xs) - x1)
    return x1


# Test the function
xs = [1, 2]
x = find_zero(xs)
print("The solution is:", x)

# Test the function again with a polynomial of a different form
xs = [6, 11, -6, 1]
x = find_zero(xs)
print("The solution is:", x)
```
The script defines a function `find_zero` that finds the roots of a polynomial. It does this by finding the root of the polynomial of the form `x^n` which is the largest term in the polynomial `xs` that is not equal to zero.

The script then tests the function with two different polynomials and prints the corresponding solutions.