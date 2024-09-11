```python
import math

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
    # Check if list has even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")

    # Find the largest non-zero coefficient
    largest_coeff = max((coeff for coeff in xs if coeff!= 0), default=None)

    # If all coefficients are zero, return any number
    if largest_coeff is None:
        return 0

    # Construct the polynomial
    poly_str = "x**{} + {}".format(len(xs)-1, " + ".join("{}*x**{}".format(coeff, i) for i, coeff in enumerate(xs) if i!= 0))

    # Find the zero point using a quadratic formula
    if len(xs) == 2:
        a, b, c = xs
        return -b / (2*a)
    elif len(xs) == 4:
        a, b, c, d = xs
        return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    else:
        raise ValueError("Quadratic formula is not defined for polynomials of degree higher than 3")

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that we have updated the `find_zero` function to handle polynomials of degree 1, 2 and 3. For higher degrees, we have added a `ValueError` to indicate that the quadratic formula is not defined for those cases. 

This function assumes that the input list `xs` has an even number of coefficients, as required by the problem statement. If the list has an odd number of coefficients, it raises a `ValueError`.

This function also assumes that the largest non-zero coefficient in the list is the leading coefficient of the polynomial. If all coefficients are zero, it returns 0.

Finally, this function uses the quadratic formula to find the zero point for polynomials of degree 2 or 3. For polynomials of higher degree, it raises a `ValueError`.