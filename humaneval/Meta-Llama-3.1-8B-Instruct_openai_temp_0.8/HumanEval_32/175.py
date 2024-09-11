### Solving Polynomial Equations using Python

Below is a Python script that uses the `numpy` library to solve polynomial equations.

```python
import numpy as np


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * np.power(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.
    x is guaranteed to be a root, even if there are many.
    xs must have an even number of coefficients and the largest non-zero coefficient.
    """
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    if len(xs) > 0 and xs[0] == 0:
        raise ValueError("xs must have the largest non-zero coefficient as the first element")

    degree = len(xs) // 2 - 1
    coeffs = np.poly1d(xs[:degree+1])
    roots = np.roots(coeffs)

    return roots[np.isreal(roots)][0].real


# Example usage:
if __name__ == "__main__":
    print("Test 1:")
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x

    print("\nTest 2:")
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3

    print("\nTest 3: Edge case, even number of coefficients")
    print(find_zero([1, 2]))

    print("\nTest 4: Edge case, first coefficient is zero")
    try:
        print(find_zero([0, 1]))
    except ValueError as e:
        print(e)

    print("\nTest 5: Edge case, odd number of coefficients")
    try:
        print(find_zero([1, 2]))
    except ValueError as e:
        print(e)
```

Note that this code uses `numpy` to efficiently handle polynomial operations. The `poly1d` function is used to create a polynomial object from the coefficients, and the `roots` function is used to find the roots of the polynomial. The code also includes example usage and error handling to demonstrate its functionality.