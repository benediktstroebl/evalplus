```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs. Sum[ xs.
    """ sum(xs)
    + sum([pow(x, i) for i, coeff in enumerate(xs)]))

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that the polynomial is zero
    find_zero returns x
    """
    if len(xs) == 0:
        raise ValueError("No coefficients provided")
    elif len(xs) == 1:
        return xs[0]
    elif len(xs) > 1 and all(c != 0 for c in xs):
        return math.pow(x, min(xs, x))
    else:
        raise ValueError("Too many coefficients. The polynomial can't be zero")

test_poly = [1, 2, -5, -6]
test_findzero = find_zero(test_poly)
print(test_poly)
print(test_findzero)
``` 
The output will be: 
```
[1, 2, -5, -6]
x
```