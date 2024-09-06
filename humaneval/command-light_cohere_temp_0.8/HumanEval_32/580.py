```python
import math
def evaluate_poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x, returns sum of the coefficients.
    """
    return sum([ coeff * math.pow(x, i) for i, coeff in enumerate(xs) ])
    """
    return sum([ coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes the polynomial equal to zero, returns only the zero root.
    if len(xs) % 2 == 0:
        return round(evaluate_poly(xs, x), 2)
    else:
        return round(evaluate_poly(xs, x), 1)
    """

xs = [1, 2]
result = find_zero(xs)
print(result)  # expected output 1.0
```

This Python script defines a function `find_zero` that finds the root of a polynomial equation with coefficients `xs` that makes the polynomial equal to zero. The script then tests the function by providing coefficients in the `xs` list and prints the result, which should be the root of the polynomial.