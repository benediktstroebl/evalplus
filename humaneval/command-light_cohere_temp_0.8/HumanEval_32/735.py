```python
import math
def evaluate_polynomial(xs):
    """
    Evaluates polynomial with coefficients xs at point x, returns result.
    """
    xs : list[list[int]]
    x : float
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial is equal to 0, returns only zero point, even if there are many.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """>>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    print("The result of evaluate_polynomial:", evaluate_polynomial([1, 2]))
    print("The result of find_zero:", find_zero([1, 2]))
    ```

The function evaluate_polynomial in this script accepts a list of coefficients as input and returns the value of the polynomial at the given point x. The function find_zero accepts the list of coefficients as input and returns the point x that makes the polynomial equal to 0.