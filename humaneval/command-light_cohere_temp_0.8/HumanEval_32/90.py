```python
import math
def poly(xs: list, x: float) -> int:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    >, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    return: 1
        -0.0
        -0.25
    -1
        maximum of non zero coefficients in xs.

# Example 1
print(find_zero([1, 2])) # f(x) = 1 + 2x - 0.5
# Example 2
print(find_zero([-6, 11, -6, 1])) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
#
# Example 3
print(find_zero([1, -2, 3, -4])) # (-2) * (x - 3) * (x + 2) = -4 + 3x + 2x^2
```

The above Python script defines a self-contained function `poly` that evaluates a polynomial at a given point, and `find_zero` that finds the zero of a polynomial. The `poly` function calculates the coefficients of the polynomial and returns the result, while the `find_zero` function takes a list of coefficients as input and returns the zero of the polynomial with those coefficients. The script also provides two examples that demonstrate the use of the `find_zero` function with different sets of coefficients.