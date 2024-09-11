### Evaluating Polynomials and Finding Zeroes
```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * np.power(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Validate input coefficients
    if not xs or (len(xs) % 2!= 0):
        raise ValueError("List must have even number of coefficients")

    n = len(xs)
    if not any(coeffs for coeffs in xs):
        raise ValueError("List must have at least one non-zero coefficient")

    # Determine the index of the largest non-zero coefficient
    max_idx = max(i for i, x in enumerate(xs) if x!= 0)

    # Create a new polynomial with the maximum coefficient as the constant term
    new_xs = [xs[max_idx]] + xs[:max_idx]

    # Calculate the root using the quadratic formula
    a, b, c = new_xs[-3], new_xs[-2], new_xs[-1]
    disc = np.sqrt(b**2 - 4*a*c)
    root = (-b + disc) / (2 * a)

    return root


# Test cases
print("Test case 1:")
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print("Test case 2:")
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
Note: The `numpy` library is used for the `np.power` function, which is more efficient than the `math.pow` function. Also, I added some error checking to ensure that the input list has an even number of coefficients and at least one non-zero coefficient.