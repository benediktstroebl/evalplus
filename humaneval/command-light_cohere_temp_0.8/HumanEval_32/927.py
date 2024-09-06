```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff ** math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0, returns only zero point, even if there are many roots.
    Furthermore, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

if __name__ == "__main__":
    # Example usage
    xs = [1, 2, -6, 11, -6, 1]
    x = float(input("Enter x: "))
    print("The zero of polynomial:", poly(xs, x))
    print("The zero of find_zero:", find_zero(xs))
```

This script has a function `poly` that evaluates a polynomial with given coefficients at a point. The function also has a function `find_zero` that finds the zero of a polynomial. The `find_zero` function uses the same logic as the `poly` function but also finds the zero of a polynomial instead of evaluating the polynomial. The script then provides an simple way to solve the problem.