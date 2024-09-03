```python
def derivative(xs: list):
    """
   xs represent coefficients of a polynomial
    Derivative of polynomial is given by: f'(x) = sum(coefficient * x^n)
    -> Get the derivative of the polynomial in the same form
    """
    derivative_list = [xs[0] + xs[1] * x, xs[0] + xs[2] * x**2 + xs[3] * x**3]
    return derivative_list
```
The function `derivative` takes a list `xs` as an argument which represents the coefficients of a polynomial. Each element in `xs` is added together to the corresponding term in the derivative.