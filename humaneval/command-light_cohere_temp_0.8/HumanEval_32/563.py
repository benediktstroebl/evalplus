```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # Use, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return [x[0]
    """
    return math.floor(math.exp(find_zero(xs)/math.log(len(xs)))


# Test the function with a few examples:
xs = [1, 2]
x = 0.5
result = poly(xs, x)
print("poly result:", result)

xs = [-6, 11, -6, 1]
x = 1
result = poly(xs, x)
print("poly result:", result)

xs = [2, 2, 2, 3]
x = -3
result = poly(xs, x)
print("poly result:", result)

xs = [1, -1, 2]
x = 0
result = find_zero(xs)
print("find_zero result:", result)
```
This Python script defines a function poly that computes a polynomial using the coefficients provided as input. The find_zero function finds the zero of the polynomial, i.e., the values at which polynomial equals zero. The script then tests the function with a few examples, showcasing how to use these functions to evaluate polynomial results and find zeros.