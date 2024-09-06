```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *x value of i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0,
    find_zero returns only zero point, even if there are many.
    find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
    best solution
    - x = 1.414
    -6
    6.;;
    -1.4400000000000000
    value of f(x) = x**6 - 6598931288400000*x^5 + 878493458840400000*x^4 - 4021216504030400000*x^3 + 1290625404040400000*x^2 - 11806801698400000*x + 62909146945449321.4000000000000005
   Departing from the leading exponent in f(x) that makes the polynomial hard to solve. The largest coefficient is -13064824441683505490484477, which is -5e+06, which is much smaller than the leading exponent in f(x). So we know that we can use the leading coefficient to find the solution.
    ```xs = [1, 2]
    x = 1.0
    # result = 1 + 2x
    print(result)
    """

Let's check the result:
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *value of i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0,
    find_zero returns only zero point, even if there are many.
    #         Nonex, but find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

```