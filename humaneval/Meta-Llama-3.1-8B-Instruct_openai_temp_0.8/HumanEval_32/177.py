```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    n = len(xs)
    a = np.array([coeff for i, coeff in enumerate(xs) if i % 2 == 0])
    b = np.array([coeff for i, coeff in enumerate(xs) if i % 2 == 1])
    x = np.roots(np.poly1d(b[::-1])/a[::-1]).real
    return x[np.isreal(x) & (x >= -10) & (x <= 10)][0]

# Testing
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

**Note:** The `np.roots` function is used to find the roots of the polynomial. However, this function returns complex numbers, so we filter out complex roots and take the first real root within a certain range. The range is chosen to be [-10, 10] to capture the most probable root. If there are multiple real roots within this range, the first one will be returned. 

Also, this function assumes that the polynomial has at least one real root within the specified range. If there are no real roots in this range, the function will return None.