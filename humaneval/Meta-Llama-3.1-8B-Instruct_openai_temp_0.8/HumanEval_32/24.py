```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    n = len(xs)
    assert n % 2 == 0, "List xs must have even number of coefficients"
    assert any(coeff!= 0 for coeff in xs), "List xs must have largest non-zero coefficient"
    # Newton-Raphson method to find root of polynomial
    def derivative(xs):
        return [i * coeff for i, coeff in enumerate(xs[:-1])]
    
    def f(x):
        return poly(xs, x)
    
    def df(x):
        return poly(derivative(xs), x)
    
    x = -xs[1]/xs[0] # initial guess
    while abs(f(x)) > 1e-5: # stop when f(x) is close to 0
        x = x - f(x) / df(x)
    return round(x, 2)

# Test cases
print(find_zero([1, 2]))  # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the Newton-Raphson method to find the root of the polynomial. This method starts with an initial guess and iteratively refines it until the function value is close to zero. The `derivative` function calculates the derivative of the polynomial, and the `f` and `df` functions calculate the function and its derivative at a given point.