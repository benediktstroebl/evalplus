```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + ... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.

    If xs has even number of coefficients, then the largest non zero coefficient guarantees that there is a solution
    """
    return math.floor(find_zero(xs, x=0.0))

poly([1, 2]) # f(x) = 1 + 2x
-0.5
find_zero([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
-1.0
find_zero([4, 6, 8, 4, 4]) # 4x^4 + 6x^3 + 8x^2 + 4x^2 + 4x
-2.0

This Python script defines a polynomial function and a function to find the zeros of a polynomial. The polynomial function takes a list of coefficients and a point x as input and returns the polynomial evaluated at x. The function to find the zeros of a polynomial takes a list of coefficients as input and returns the zero point x, which satisfies the polynomial equation. 
In this script, the polynomial function is used to evaluate a polynomial with the coefficients [1, 2] at the point x = -0.5, which returns 1 + 2x + 2x^2 + (-6) * x^3. The function to find the zeros then takes a list of coefficients as input and returns the zero point x, which satisfies the polynomial equation. The function then finds the zeros for the polynomial with coefficients [4, 6, 8, 4, 4] at the point x = -2.0, which returns 2x, -6.5, and -12, -4.