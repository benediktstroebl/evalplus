```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    and returns xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.

if __name__ == "__main__":
    xs = [1, 2] # coefficients of a polynomial
    x = 2.0  # evaluate polynomial at x and return the result
    assert(poly(xs, x) == 1.0)
   
    print(xs) # coefficients of a polynomial
    find_zero(xs)
    assert(find_zero(xs) == [1, 2])  # find zero of polynomial
    print(x) # evaluate x at zero point
    assert(x - 1.0 == 0)  # evaluate polynomial at zero and return the result
    ```