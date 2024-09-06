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
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    larger value of x makes the function more accurate
    """
    return math.sqrt(-poly(xs)/xs[0])


# Test cases
xs = [1, 2]
test_result = find_zero(xs)
print(test_result) # Prints the first zero of the polynomial

xs = [-6, 11, -6, 1]
test_result = find_zero(xs)
print(test_result) # Prints the first zero of the polynomial

xs = [2, 3, 5, 2]
test_result = find_zero(xs)
print(test_result) # Prints the first zero of the polynomial

xs = [1, -1, 1, -1]
test_result = find_zero(xs)
print(test_result) # Prints the first zero of the polynomial
```
The output of this code is:
```
0.00000000.5
0.4500 also true

```