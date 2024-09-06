```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes the polynomial equal to zero, returns only the root(s) of this equation, and also returns a list of these roots.
    ensure_even_coefficients(xs):
        if len(xs) % 2 == 1:
            raise ValueError("The list must have an even number of coefficients.")
    roots: list = []
    for x in range(len(xs)):
        if xs[x] == 0:
            roots.append(x(x))
    return roots
if __name__ == "__main__":
    xs = [1, 2]
    x = 2.0
    roots = find_zero(xs)
    print("The roots of the polynomial are : ", roots)
    ```