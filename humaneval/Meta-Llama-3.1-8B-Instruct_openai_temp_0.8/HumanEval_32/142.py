**Polynomial Evaluation and Root Finding**
=============================================

Below is a self-contained Python script that implements the `poly` function for evaluating polynomials and the `find_zero` function for finding zeros of a polynomial.

```markdown
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
        xs (list): List of coefficients of the polynomial in descending order of power.
        x (float): Point at which the polynomial is evaluated.
    
    Returns:
        float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of the polynomial defined by xs.
    
    Args:
        xs (list): List of coefficients of the polynomial in descending order of power.
                  The list must have an even number of coefficients and the largest coefficient must be non-zero.
    
    Returns:
        float: A zero of the polynomial.
    """
    n = len(xs)
    assert n % 2 == 0, "Coefficient list must have an even number of coefficients."
    assert xs[0]!= 0, "Largest coefficient must be non-zero."

    # Check if the polynomial is a constant (x^0)
    if n == 1:
        return 0

    # Check if the polynomial is a linear function (x^1)
    if n == 2:
        return -xs[1] / xs[0]

    # Divide the polynomial by the largest coefficient
    xs = [coeff / xs[0] for coeff in xs]

    # Find the zero using the quadratic formula
    a = xs[2]
    b = xs[1]
    c = xs[0]
    D = b**2 - 4*a*c
    if D < 0:
        raise ValueError("No real solutions exist.")
    elif D == 0:
        return -b / (2*a)
    else:
        return (-b + math.sqrt(D)) / (2*a)
```

**Example Usage:**

```python
# Evaluate the polynomial f(x) = 1 + 2x at x = 2
print(poly([1, 2], 2))

# Find a zero of the polynomial g(x) = -6 + 11x - 6x^2 + x^3
print(round(find_zero([-6, 11, -6, 1]), 2))
```

In this script, we first implement the `poly` function to evaluate a polynomial at a given point. Then, we implement the `find_zero` function to find a zero of the polynomial. The `find_zero` function assumes that the input list of coefficients has an even number of coefficients and the largest coefficient is non-zero. It then divides the polynomial by the largest coefficient and finds the zero using the quadratic formula.