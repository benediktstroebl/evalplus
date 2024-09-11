```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    
    Parameters:
    xs (list): coefficients of the polynomial

    Returns:
    float: a zero point of the polynomial
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("The list xs must have an even number of coefficients")

    # Find the largest non-zero coefficient
    while not xs[-1] and len(xs) > 1:
        xs.pop()

    # Find a solution using the largest non-zero coefficient as a factor
    a = xs[-1]
    b = xs[-2]
    if a!= 0:
        return -b/(2*a)
    elif b == 0:
        return 0
    else:
        # In case of x^2 term only
        return -poly(xs[:-1], 0) / xs[-2]

# Example usage:
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that the `find_zero` function uses an efficient method to find a zero point, assuming that the input polynomial has a factor of the form `ax^2 + bx + c` with `a!= 0`. If the input polynomial is of degree 2 or more, this method will only find one zero point, even if there are multiple zero points. 

Also note that due to the `math.pow(x, i)` calls, this code may be inefficient for large polynomials or large values of `x`. For such cases, consider using a numerical library like SciPy or a specialized polynomial library.