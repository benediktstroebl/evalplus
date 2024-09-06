```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x, returns sum of coefficients.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and, it finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    minimum_error
    """
    def find_zero(xs):
        non_zero_coefficients = []
        for coeff in xs:
            if coeff != 0:
                non_zero_coefficients.append(coeff)
        # sort coefficients in ascending order
        coefficients = sorted(non_zero_coefficients)
        # sort coefficients in descending order of power
        coefficients.sort(reverse=True)
        # find zero of polynomial with coefficients in ascending order
        n = len(coefficients)
        power = 1
        x = 0
        while n:
            x += coefficients[n - 1] * power
            power += 1
        return x

```