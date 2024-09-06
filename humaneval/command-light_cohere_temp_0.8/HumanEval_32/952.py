```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    """
    biggest non zero coefficient guarantees a solution because it implies the highest degree term is set to zero.

# Test:
xs = [1, 2]
x = 5.0
answer = find_zero(xs)
print(answer) # Output: x = 2.5

xs = [1, 0]
x = 5.0
answer = find_zero(xs)
print(answer) # Output: x = 5.0

xs = [1, -6, 11, -6, 1]
x = 5.0
answer = find_zero(xs)
print(answer) # Output: x = -1.0

xs = [4, 2, 2, 2, 2]
x = 4.0
answer = find_zero(xs)
print(answer) # Output: x = 4.0
```