```markdown
### Evaluating Polynomials and Finding Zero Points

This script defines two functions: `poly` for evaluating a polynomial at a given point, and `find_zero` for finding a zero point of a polynomial given its coefficients.

#### Requirements
Python 3.x

#### Code

```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    result = 0
    for i, coeff in enumerate(xs):
        result += coeff * (x ** i)
    return result


def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    # validate input: even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("Number of coefficients must be even")

    # find the largest non-zero coefficient
    largest_non_zero_coeff = max(coeff for coeff in xs if coeff!= 0)

    # find the index of the largest non-zero coefficient
    largest_non_zero_index = xs.index(largest_non_zero_coeff)

    # find the root of the polynomial
    root = -xs[largest_non_zero_index + 1] / (xs[largest_non_zero_index] * 2)
    return root


# Example usage
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

#### Explanation
The `poly` function evaluates a polynomial at a given point by summing the products of the coefficients and the corresponding powers of x.

The `find_zero` function finds a zero point of a polynomial given its coefficients. It first validates the input to ensure that the number of coefficients is even. Then, it finds the largest non-zero coefficient and its index. Finally, it calculates the root of the polynomial using the quadratic formula.

Note that this implementation assumes that the largest non-zero coefficient is at an even index, which guarantees a solution. If there are multiple roots, this function will only return one.