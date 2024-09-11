```markdown
## Polynomial Root Finder
### Problem Statement
Evaluate polynomial with coefficients `xs` at point `x` and find the zero point of a given polynomial.

### Code
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    
    :param xs: list of coefficients of a polynomial
    :return: zero point of the polynomial
    """
    # Ensure the input list has an even number of coefficients
    assert len(xs) % 2 == 0, "List xs must have an even number of coefficients"
    
    # Find the index of the largest non-zero coefficient
    max_idx = next(i for i, coeff in enumerate(xs) if coeff!= 0)
    
    # Synthetic division to find the zero point
    zero = -xs[max_idx - 1] / xs[max_idx]
    
    return zero


# Example usage
print("Example 1:")
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x

print("\nExample 2:")
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

### Explanation
The `find_zero` function uses synthetic division to find the zero point of the polynomial. It first ensures that the input list has an even number of coefficients. Then, it finds the index of the largest non-zero coefficient. The zero point is then calculated using the formula `-xs[max_idx - 1] / xs[max_idx]`.

Note that this implementation assumes that the polynomial has a root at the calculated point. If the polynomial does not have a root at this point, the function may return incorrect results.