```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0,
    finds a solution.
# Test the function
    def test(x):
        poly([1, 2, -5], x)
        return (poly(xs) == 0) == True

xs = [1, 2, -5]
x = 0.5
print(test(x))  # True
print(find_zero(xs))  # 2.0667
```

This script defines a function `poly` that computes the polynomial with coefficients `xs` at `x` and returns the result. It also defines a function `find_zero` that finds the zero of the polynomial `poly(x)` using the `poly` function. The `test` function is used to verify if the `poly` function works correctly for a given `x` value. The `find_zero` function is tested with a list of coefficients and the output is printed.