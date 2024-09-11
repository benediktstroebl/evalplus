### Python Script: Finding Zero of a Polynomial
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    This function returns only one zero point, even if there are many.
    It only takes lists xs having an even number of coefficients
    and largest non zero coefficient as it guarantees a solution.

    Parameters:
    xs (list): Coefficients of a polynomial.

    Returns:
    float: The zero point of the polynomial.
    """
    # Ensure the list has an even number of coefficients
    if len(xs) % 2 == 1:
        raise ValueError("The list of coefficients must have an even number of elements.")

    # Make a copy of the list and append zeros at the end
    # This is to ensure that the polynomial has the same degree as the number of coefficients
    # For example, [1, 2] should be treated as [1, 2, 0, 0]
    xs = xs + [0] * (len(xs) % 2)

    # Find the largest non-zero coefficient
    non_zero_coeffs = [coeff for coeff in xs if coeff!= 0]
    largest_non_zero_coeff = max(non_zero_coeffs)

    # Find the index of the largest non-zero coefficient
    idx = [i for i, coeff in enumerate(xs) if coeff == largest_non_zero_coeff][0]

    # Find the zero point by dividing the leading coefficient by the constant term
    # We use numpy roots function to find the roots of the polynomial
    # The roots function returns an array of roots, so we take the first root
    coefficients = np.poly1d(xs)
    roots = np.roots(coefficients)
    zero_point = [root.real for root in roots if np.isclose(root.imag, 0, atol=1e-10)][0]

    return zero_point

# Test the function
print("Test 1:")
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print("Test 2:")
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script first ensures that the list of coefficients has an even number of elements. It then makes a copy of the list and appends zeros at the end to ensure that the polynomial has the same degree as the number of coefficients. The largest non-zero coefficient and its index are found. The zero point is then found by dividing the leading coefficient by the constant term using numpy's roots function. The function returns only one zero point, even if there are many.