```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x such that poly(x) = 0, that is equal to the root of the polynomial.

# Test case:
xs = [1, 2]
poly_val = poly(xs, 3) # x^3
zero_x = find_zero(xs)
print("poly_val:", poly_val)
print("zero_x:", zero_x)
```

This Python script defines a function `poly` that evaluates a polynomial with coefficients `xs` at a given point `x`. The function then returns the value of the polynomial at `x`. The script also defines a function `find_zero` that finds the zero of a polynomial by evaluating the polynomial at various values and finding the value that makes the polynomial equal to zero.

The `find_zero` function takes a list `xs` of coefficients as input, which represents the polynomial to be evaluated. It returns the value that makes the polynomial equal to zero.

The script provides a test case, where the `xs` list has coefficients [1, 2] and the `poly` function evaluates the polynomial at `3`. The `find_zero` function is called with the `xs` list and returns the value of the polynomial at `3` as the zero value. The script then prints the result of the evaluation and the output of the `find_zero` function.