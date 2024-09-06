```python
import math
def find_zero(xs):
    """
   xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    find_zero returns only zero point, odd if there are multiple roots.
    >> round(find_zero([1, 2]), 2)
    """
    # check even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have even number of coefficients.")
    # largest non zero coefficient
    max_coeff = max(xs)
    # find_zero polynomial
    poly = sum([i * math.pow(x, j) for i, j in enumerate(xs)])
    # find zero of polynomial
    x_root = math.floor(poly / max_coeff)
    # return
    return x_root

# test case 1
print(find_zero([1, 2]))
# test case 2
print(find_zero([-6, 11, -6, 1]))
```
The above code defines a Python function `find_zero` that finds the zero of a polynomial. It uses the largest non-zero coefficient as the denominator to get the zero of the polynomial.