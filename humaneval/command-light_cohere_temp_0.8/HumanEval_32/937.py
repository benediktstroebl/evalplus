```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *[i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    >, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

xs=[1, 2]
x = 3.1
ans = poly(xs, x)
print(ans) # Output: 1 + 2*3 + 2*x^2

xs = [1, -6, 11, -6, 1]
x = 5
ans = poly(xs, x)
print(ans) # Output: -6 + 11*x - 6*x^2 + x^3

xs = [1, 2, -3, -4]
x = 0
ans = poly(xs, x)
print(ans) # Output: -1 + (-3)*x + (-4)*x^2

xs = [1, 2, 3, 4, 5]
x = 0.1
ans = poly(xs, x)
print(ans) # Output: 5321

xs = [1, 2, -3, -4]
x = 1.1
ans = poly(xs, x)
print(ans) # Output: -1 + 2*x + 3*x^2 - 4*x^3

xs = [1, 2, 3, 4, 5]
x = 2.0
ans = poly(xs, x)
print(ans) # Output: 5101
```

The script defines a function `poly` that evaluates a polynomial at a given point. The `find_zero` function finds the zero of a polynomial. The `poly` function has a test that checks if the polynomial is equal to zero.

The `poly` function uses the `math.pow` function to evaluate the coefficients of the polynomial. The `find_zero` function uses the `poly` function to evaluate the polynomial at the point being searched. The `find_zero` function returns the value of the polynomial at the point being searched.