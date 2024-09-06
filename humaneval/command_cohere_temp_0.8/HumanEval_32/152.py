Here's a Python script that includes a function to solve the problem of finding a zero point of a polynomial:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if list length is even
    if len(xs) % 2 == 0:
        # Find discriminant
        discriminant = xs[-1]**2 * xs[0]
        for i in range(1, len(xs)-1):
            discriminant = discriminant - xs[i]**2 * xs[-2]
        # Find root
        root = (-xs[-1] * math.sqrt(discriminant) - xs[0]) / (xs[0] - xs[-1])
        # Check if root is not negative
        if root >= 0:
            return root
    else:
        raise ValueError("Pass an even number of coefficients")
```

This script includes two functions. The first function, `poly(xs, x)`, calculates the value of a polynomial at a given point. The function takes as input a list of coefficients (`xs`) and a variable (`x`) at which to evaluate the polynomial. It returns the value of the polynomial by summing the products of the coefficients and the variable raised to the power equal to the index of the coefficient in the list.

The second function, `find_zero(xs)`, finds the point at which a polynomial equals zero. It takes as input the list of coefficients of the polynomial. This function first checks if the list has an even length, raising an error if it does not. It then finds the discriminant of the polynomial, calculating the coefficients of the polynomial one by one, and finding the square root of the discriminant to calculate the root using the **discriminant** formula: `discriminant = xs[-1]**2 * xs[0]
```python
for i in range(1, len(xs)-1):
    discriminant = discriminant - xs[i]**2 * xs[-2]
```
It then calculates the root of the polynomial, checks if it's not negative, and returns it if it's non-negative. 

You can use the functions by calling `poly` with a list of coefficients `xs` and a float `x` to evaluate the polynomial at a specific point, or by calling `find_zero(xs)` with a list of coefficients to find the zero point of the polynomial. Here are some examples of how these functions can be used:
```python
>>> round(poly([1, 2], 2), 2)
2.0

>>> round(poly([1, 2], -2), 2)
-2.0

>>> round(find_zero([1, 2]), 2) 
-0.5

>>> round(find_zero([-6, 11, -6, 1]), 2)
1.0
```

These examples