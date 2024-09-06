```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    find_zero returns only zero point, odd if there is no solution, otherwise, finds and returns the zero point of the polynomial with even number of coefficients, largest non-zero coefficient as it guarantees a solution.
    ```

# Example 1
xs = [1, 2]
xs = [x + 1, x + 2]
poly_value = poly(xs, x)
print(f"{poly_value}")
zero_point = find_zero(xs)
print(f"{zero_point}")

# Example 2
xs = [1, -6, -6, 1]
xs = [-6, 11, -6, 1]
poly_value = poly(xs, x)
print(f"{poly_value}")
zero_point = find_zero(xs)
print(f"{zero_point}")
```

The above Python script defines a function `poly` that computes the value of a polynomial with given coefficients at a given point `x`. It also defines a function `find_zero` that finds the zero point of a polynomial, which is the value of `0` in the polynomial. The script then demonstrates these two examples of how to use the `poly` and `find_zero` functions.