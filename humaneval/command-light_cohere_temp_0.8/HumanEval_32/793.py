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
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # Test case: x -2 = 1 +-4 
    # Test cases: [1, 2] 
    # Test cases: [-6, 11, -6, 1]
    # Test cases: [2, 3, -1]
    # Test cases: [0, 0, -2]
    # Test cases: [-1, 0, 0] 
    return round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x -0.5
```

The provided code defines a Python function `poly` that computes the value of a polynomial with a given list of coefficients `xs` at a point `x`. The `poly` function calculates the polynomial's value by summing the product of each coefficient multiplied with the corresponding power of `x` up to `n`. 

The `find_zero` function finds the zero of the polynomial. 

It takes a list of coefficients `xs` as input and returns the value of `x` that makes the polynomial equal to zero. 

The `find_zero` function uses the polynomial equation `poly(x) = 0` to find the zero of the polynomial.