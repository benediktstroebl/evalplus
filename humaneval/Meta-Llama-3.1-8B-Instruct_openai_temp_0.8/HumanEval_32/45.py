### Evaluating Polynomials and Finding Zeroes

Below is a Python script that implements the `poly` and `find_zero` functions:
```markdown
### Polynomial Evaluation and Zero Finding
```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    This function only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    # Ensure the polynomial is monic (leading coefficient is 1)
    xs = [coeff / xs[0] for coeff in xs]
    
    # Use numpy's roots function to find the roots of the polynomial
    roots = np.roots(xs)
    
    # Find the real root with the smallest absolute value
    real_roots = [root for root in roots if root.imag == 0]
    zero = min(real_roots, key=lambda x: abs(x))
    
    return round(zero.real, 2)


# Test cases
import math

# Original test cases
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3

# Additional test cases
print(find_zero([1, -3, 2])) # f(x) = 1 - 3x + 2x^2
```
Note that I've used `numpy` to find the roots of the polynomial, as it is more efficient and accurate than a simple numerical method. I've also modified the `find_zero` function to only consider the real roots of the polynomial, and to return the root with the smallest absolute value. This ensures that the function will return a single value, even if there are multiple roots.