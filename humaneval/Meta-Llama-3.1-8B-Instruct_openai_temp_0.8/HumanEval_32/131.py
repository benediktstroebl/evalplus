### Finding a Zero of a Polynomial
#### Python Script

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): Coefficients of the polynomial.
    x (float): Point at which to evaluate the polynomial.

    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial. The largest non-zero coefficient must be at the beginning of the list.

    Returns:
    float: A zero of the polynomial. If there are multiple zeros, this function may not find the correct one.

    Raises:
    ValueError: If the list of coefficients does not have an even number of elements.
    """
    if len(xs) % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements.")

    # Use numpy's roots function to find the zeros of the polynomial
    coefficients = xs[::-1]  # Reverse the list to match numpy's convention
    roots = np.roots(coefficients)

    # If there are real zeros, return the first one
    real_roots = [root.real for root in roots if root.imag == 0]
    if real_roots:
        return round(real_roots[0], 2)
    else:
        # If there are no real zeros, return None
        return None


# Test the function
if __name__ == "__main__":
    print(find_zero([1, 2]))  # f(x) = 1 + 2x
    print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the `numpy` library to find the zeros of the polynomial. The `np.roots` function returns all the zeros of the polynomial, and we then filter out the real zeros. If there are multiple real zeros, this function may not find the correct one.

Note that this function assumes that the largest non-zero coefficient is at the beginning of the list, as specified in the problem. If the coefficients are not in this order, you will need to reverse the list before passing it to the `find_zero` function.

Also note that this function returns the first real zero it finds, which may not be the correct zero in all cases. If you need to find all the zeros of the polynomial, you will need to modify the function accordingly.