### Polynomial Zero Finder

Below is a Python script that implements the `poly` and `find_zero` functions for finding the zero of a polynomial with given coefficients.

```markdown
### polynomial_zero_finder.py

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): List of coefficients of the polynomial.
    x (float): Point at which to evaluate the polynomial.

    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial with given coefficients.

    Args:
    xs (list): List of coefficients of the polynomial, where the largest non-zero coefficient is first.

    Returns:
    float: A point x such that poly(x) = 0.
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2 == 1:
        raise ValueError("The list of coefficients must have an even number of elements")

    # Find the largest non-zero coefficient index
    largest_non_zero_idx = next(i for i, x in enumerate(xs) if x!= 0)

    # Initialize the coefficients of the polynomial to find a zero
    new_xs = [-coeff for coeff in xs[:largest_non_zero_idx][::-1] + xs[largest_non_zero_idx:][::-1]]

    # Use numpy's roots function to find all zeros
    zeros = np.roots(new_xs)

    # Return the real zero if it exists, otherwise return the first real zero
    for zero in zeros:
        if zero.imag == 0:
            return zero.real
    return zeros[np.isreal(zeros)][0].real

# Example usage:
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script first checks if the list of coefficients has an even number of elements. It then finds the largest non-zero coefficient index and constructs a new list of coefficients by reversing the first part of the list up to the largest non-zero coefficient and the second part of the list. The `numpy.roots` function is then used to find all zeros of the new polynomial. If no real zero exists, it returns the first real zero.