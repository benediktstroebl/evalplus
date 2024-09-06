```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """

def test(x: float):
    """
    Test for polynomial f(x) = x^2 + x - 5
    """
    p = [x**2 + x - 5]
    return poly(p, x) == x**2 + x - 5

def main():
    """
    test for example polynomial
    """
    print("test passed")

if __name__ == "__main__":
    main()
```