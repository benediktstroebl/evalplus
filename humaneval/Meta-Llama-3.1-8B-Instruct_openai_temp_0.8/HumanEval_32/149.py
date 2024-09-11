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
    Finds a zero point of a polynomial with coefficients xs.
    xs are coefficients of a polynomial in descending order of degrees.
    xs are expected to have even number of coefficients.
    """
    if len(xs) % 2 == 1:
        raise ValueError("Polynomial with odd number of coefficients has no real zeros")
    
    # Use numpy roots function to find all zeros of the polynomial
    coefficients = np.poly1d(xs).c
    roots = np.roots(coefficients)
    
    # Return the zero with the smallest absolute value
    return round(roots[np.argmin(np.abs(roots))].real, 2)


# Test cases
if __name__ == "__main__":
    print(find_zero([1, 2]))  # f(x) = 1 + 2x
    print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

In this code, I've used the `numpy` library to find the roots of the polynomial. This is a more robust and efficient way to find the zeros of a polynomial, especially for larger polynomials. The `poly1d` function is used to convert the list of coefficients into a numpy polynomial object, and then the `roots` function is used to find all the zeros of the polynomial. The zero with the smallest absolute value is then returned.

I've also added a check to ensure that the list of coefficients has an even number of elements, as required by the problem statement. If the list has an odd number of elements, a `ValueError` is raised.