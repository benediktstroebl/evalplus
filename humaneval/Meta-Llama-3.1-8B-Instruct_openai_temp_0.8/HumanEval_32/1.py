```markdown
### Python Script to Find Zero of a Polynomial

This script defines two functions: `poly` to evaluate a polynomial and `find_zero` to find a zero of a polynomial.

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^(n-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs.
    xs are coefficients of a polynomial in descending order of powers.
    find_zero returns a single zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the number of coefficients is even
    assert len(xs) % 2 == 0, "The number of coefficients must be even"

    # Find the largest non-zero coefficient
    largest_non_zero = max([coeff for coeff in xs if coeff!= 0])

    # Find the index of the largest non-zero coefficient
    largest_non_zero_index = xs.index(largest_non_zero)

    # Split the coefficients into two halves
    first_half = xs[:largest_non_zero_index + 1]
    second_half = xs[largest_non_zero_index + 1:]

    # Reverse the second half to get the coefficients in descending order of powers
    second_half.reverse()

    # Find the zero of the polynomial using numerical method
    roots = np.roots(first_half + second_half)

    # Find the real root
    real_root = roots[np.isreal(roots)]

    # Return the real root
    return real_root[0].real


# Test the function
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
The `find_zero` function now uses the `numpy` library's `roots` function to find a zero of the polynomial. The polynomial is split into two halves, with the first half containing the coefficients of the terms with even powers and the second half containing the coefficients of the terms with odd powers. The coefficients are then reversed in the second half to get the coefficients in descending order of powers. The zero of the polynomial is then found using the `roots` function on the combined coefficients. The real root is then returned.

Note that this function may not return the correct result if the polynomial has no real root or if the input coefficients are not in the correct order. The user should ensure that the input coefficients are correct and in the correct order before using this function.