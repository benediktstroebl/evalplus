```markdown
## Evaluating Polynomials and Finding Zero Points
### Overview

This script provides two functions: `poly` to evaluate a polynomial at a given point and `find_zero` to find a zero point of a polynomial.

### Code
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
    Finds a zero point of a polynomial.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        float: A zero point of the polynomial.

    Raises:
        ValueError: If the list xs does not have an even number of coefficients.
    """
    if len(xs) % 2!= 0:
        raise ValueError("List xs must have an even number of coefficients")

    # Assuming the largest non-zero coefficient guarantees a solution
    max_non_zero_coeff = [coeff for coeff in xs if coeff!= 0]
    max_non_zero_coeff = max(max_non_zero_coeff)
    index = xs.index(max_non_zero_coeff)
    x = -1 * math.pow(max_non_zero_coeff, -1) / (index)

    return round(x, 2)

# Example usage
if __name__ == "__main__":
    print(find_zero([1, 2]))  # f(x) = 1 + 2x
    print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    try:
        print(find_zero([1, 2, 3]))  # Test error handling
    except ValueError as e:
        print(e)
```

### Explanation

*   The `poly` function evaluates a polynomial at a given point `x`. It takes a list of coefficients `xs` and a point `x` as input and returns the value of the polynomial at `x`.
*   The `find_zero` function finds a zero point of a polynomial. It takes a list of coefficients `xs` as input and returns a zero point of the polynomial. It assumes that the largest non-zero coefficient guarantees a solution and uses this to calculate the zero point.
*   The script includes example usage and error handling for the `find_zero` function.