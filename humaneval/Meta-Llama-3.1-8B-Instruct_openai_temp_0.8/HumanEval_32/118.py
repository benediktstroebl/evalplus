```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given coefficients xs.
    xs are coefficients of a polynomial, xs should have an even number of coefficients.
    The largest non-zero coefficient is assumed to be at the end.
    This function returns only one zero point, even if there are many.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Coefficients xs should have an even number of coefficients.")

    # Find the largest non-zero coefficient
    largest_non_zero = max(coeff for coeff in xs if coeff!= 0)

    # Use the largest non-zero coefficient as the initial guess
    # and a small step size to start the Newton-Raphson method
    x = -xs[-1] / xs[-2]
    step_size = 1e-6

    while True:
        # Evaluate the polynomial at the current point
        y = poly(xs, x)
        
        # If the polynomial is close to zero, return the current point
        if abs(y) < 1e-9:
            return round(x, 2)
        
        # Otherwise, update the current point using the Newton-Raphson method
        dy = poly([i * coeff for i, coeff in enumerate(xs)], x) if any(coeff!= 0 for coeff in xs[1:]) else 1
        x = x - y / dy
        
        # Check if we need to adjust the step size
        delta_x = abs(x - (x - y / dy))
        if delta_x < step_size:
            step_size /= 10

# Test cases
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This code defines two functions: `poly` to evaluate a polynomial at a point, and `find_zero` to find a zero point of a polynomial using the Newton-Raphson method. The `find_zero` function takes a list of coefficients as input and returns one zero point. It assumes that the largest non-zero coefficient is at the end of the list and that the list has an even number of coefficients. If these conditions are not met, it raises a ValueError. The code also includes test cases to demonstrate its usage.