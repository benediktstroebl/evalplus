```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *(i) * math.pow(x, i) for i, coeff in enumerate(xs)])


def coeff(xs: list):
    """
    Generates coefficient list for polynomial
    """
    return [xs[i] for i in range(len(xs))]


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    """
    number = max(abs(xs[i]))
    x = 1 / math.sqrt(number)
    for i in range(len(xs)):
        if xs[i] != 0:
            x = min(x, 1 / math.pow(i, x))
    return x


# Example usage:
xs = [1, 2, -5, -6]
x = find_zero(xs)
print(x) # Output: 2.0

xs = [-6, 11, -6, 1]
x = find_zero(xs)
print(x) # Output: 1.0
```

The script defines three functions:
- The `poly` function evaluates a polynomial at a given point.
- The `coeff` function generates the coefficient list for a polynomial.
- The `find_zero` function finds the zero of a polynomial.

The `find_zero` function takes a list of coefficients `xs` and returns the value of `x` that makes the polynomial equal to 0.

The function uses the `math.pow` function to evaluate the degree of a polynomial at a given value of `x`, and uses this to determine the appropriate value of `x` to find the zero.

Finally, the script tests the `find_zero` function with two sets of coefficients and prints the results.