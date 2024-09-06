```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    return [largest non zero coefficient as it guarantees a solution.
    return round(find_zero([1, 2]), 2)
    -0.5
    return round(find_zero([-6, 11, -6, 1]), 2)
    # poly(x) = 1 + 2x -0.5
    # find_zero([1, 2])
    # print(find_zero([1, 2]))
    # f(x) = 1 + 2x -0.5
    print(find_zero([-6, 11, -6, 1]))
```

The function `find_zero` accepts a list `xs` of coefficients of the polynomial, and returns the value of `x` that satisfies the polynomial equation `poly(x) = 0`. 

The function uses the `find_zero` function from the `poly` function, which returns the value of `x` that makes the polynomial `poly(x)` equal to `0`. The `find_zero` function uses the `math.pow()` function to find the mathematical operation that returns the power of `x` to a given number.  The largest non-zero coefficient in `xs` is returned, which guarantees that there is a solution to the polynomial equation. 

The function then uses the `round()` function to round the returned `x` value to two decimal places. 

The `find_zero` function returns the value of `x` as the solution to the polynomial equation `poly(x) = 0`.