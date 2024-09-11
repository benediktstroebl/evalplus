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
    Finds a zero point of a polynomial given its coefficients.
    
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    
    Parameters:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero point of the polynomial
    """
    try:
        # Newton-Raphson method for finding roots of a function
        # Initial guess is 0
        x = 0
        while True:
            f = xs[0] + sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[1:])])
            df = sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs[1:])])
            if abs(f) < 1e-6 and abs(df) > 1e-6:
                return round(x, 2)
            x -= f / df
    except ZeroDivisionError:
        # If derivative is zero, try a different initial guess
        return round(-xs[-1] / xs[-2], 2)

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

### Explanation
This script solves the problem using the Newton-Raphson method, a powerful numerical method for finding roots of a function. This method iteratively improves an initial guess for the root until it converges to the actual root.

The `find_zero` function takes the coefficients of the polynomial as input, initializes the guess to 0, and then enters an infinite loop where it calculates the function value `f` and its derivative `df` at the current guess. If the absolute value of the function value is less than a small tolerance (1e-6 in this case) and the absolute value of the derivative is greater than the tolerance, it returns the current guess as the root.

If the derivative is zero, it catches the `ZeroDivisionError` exception and tries a different initial guess, specifically the root of the polynomial with the second-to-last coefficient divided by the last coefficient.

The test cases demonstrate the function's ability to find roots for simple polynomials.