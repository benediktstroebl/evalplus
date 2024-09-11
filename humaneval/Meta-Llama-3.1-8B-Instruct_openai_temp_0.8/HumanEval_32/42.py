### Solution
```markdown
### Problem Statement
Evaluate a polynomial at a given point and find the zero point of a polynomial.

### Solution

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
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the number of coefficients is even
    if len(xs) % 2!= 0:
        raise ValueError("The number of coefficients must be even")

    # Find the largest non-zero coefficient
    largest_non_zero_coeff = max(coeff for coeff in xs if coeff!= 0)

    # Normalize the coefficients to simplify the calculation
    normalized_xs = [coeff / largest_non_zero_coeff for coeff in xs]

    # Find the zero point by solving the quadratic equation
    a, b, c = normalized_xs[0], normalized_xs[1], -normalized_xs[2]
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        raise ValueError("The polynomial does not have a real zero point")

    zero_point = (-b - math.sqrt(discriminant)) / (2*a)

    return zero_point


# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

### Explanation
The provided solution first checks if the number of coefficients is even. If not, it raises a `ValueError`. It then finds the largest non-zero coefficient and normalizes the coefficients by dividing each coefficient by this value. This simplifies the calculation.

The solution then assumes that the polynomial is of the form `x^2 + bx + c` (since it has an even number of coefficients) and uses the quadratic formula to find the zero point. It uses the `math.sqrt` function to calculate the square root of the discriminant.

Note that this solution assumes that the polynomial has a real zero point. If the discriminant is negative, it raises a `ValueError`.