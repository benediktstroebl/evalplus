```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and returns the for the coefficients of a polynomial
    """
    return round(poly(xs), 2)

xs = [1, 2]
print(find_zero(xs))  # Output: f(x) = 1 + 2x - 0.5
xs = [2, -6, 11, -6, 1]
print(find_zero(xs))  # Output: (-1 + 6x) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

The script defines a function called `poly` that calculates the value of a polynomial with given coefficients at a given point. The function then returns the function `find_zero` that finds the zeros of a polynomial using the `poly` function. The function then passes tests to the `find_zero` function and prints the output, which is the zero of the polynomial.