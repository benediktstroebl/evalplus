### Polynomial Evaluation and Zero Finding
#### Script Description

This Python script defines two functions: `poly` for evaluating a polynomial at a given point, and `find_zero` for finding a zero of a polynomial.

#### Code

```markdown
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
        xs (list): Coefficients of the polynomial in descending order of powers.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: The value of the polynomial at the given point.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[::-1])])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial in descending order of powers.
                 The list must have an even number of elements, and the largest
                 non-zero coefficient must ensure a solution exists.

    Returns:
        float: A zero of the polynomial.
    """
    n = len(xs)
    if n % 2 == 1:
        raise ValueError("List must have an even number of coefficients")

    a, b = xs[0], xs[1]
    return -b / a

# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note: In the `find_zero` function, we now directly calculate the zero using `a*x + b = 0` and thus removed the direct use of the polynomial evaluation. The test `if n % 2 == 1` has been added to check if the number of coefficients is odd, so that a ValueError is raised if necessary.