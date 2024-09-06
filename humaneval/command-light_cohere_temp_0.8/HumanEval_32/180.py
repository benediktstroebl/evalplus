```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * *x x)
    """

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial(xs, x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    - 0.5
    x
   .split(xs) into list([x**(n-1) for x in xs if x != 0])
    l = [x for x in xs if x != 0]
    l.sort()
    0,
    x = 0
    while x < l[-1]:
        x = x + 1
        l.remove(x)
    l.append(x)
    print(f'x={x} with {xs}')
    x = 0
    l.remove(x)
    l.append(x)
    print(f'x={x} with {xs}')
    print(f'xs={xs}')

xs = [1, 2]
x = 0
poly(xs, x) # 0

xs = [1, 2,3]
x = 0
poly(xs, x) # 1

xs = [4,5]
x = 0
poly(xs, x) # 4

xs = [-6, 11, -6, 1]
x = 0
poly(xs, x) # -6

xs = [0.5, 0.5]
x = 0
poly(xs, x) # 0
```