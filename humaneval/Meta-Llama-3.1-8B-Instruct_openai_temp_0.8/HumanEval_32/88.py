### Newton-Raphson Method to Find Zero of a Polynomial
The following Python script uses the Newton-Raphson method to find a zero of a polynomial. This method is an iterative process that starts with an initial guess for the root and then iteratively converges to the root using the formula:
x_{n+1} = x_n - f(x_n) / f'(x_n)
where f'(x) is the derivative of the polynomial function.

```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def poly_derivative(xs: list, x: float):
    """
    Evaluates derivative of polynomial with coefficients xs at point x.
    return xs[1] * 1 + 2 * xs[2] * x + 3 * xs[3] * x^2 +.... n * xs[n] * x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])


def find_zero(xs: list, initial_guess: float, tolerance: float = 1e-6, max_iterations: int = 100):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    x = initial_guess
    for _ in range(max_iterations):
        # Calculate the value of the polynomial and its derivative at the current estimate
        poly_value = poly(xs, x)
        poly_derivative_value = poly_derivative(xs, x)
        
        # Check if the polynomial is zero at the current estimate
        if abs(poly_value) < tolerance:
            return x
        
        # Update the estimate using the Newton-Raphson formula
        x = x - poly_value / poly_derivative_value
    
    # If the maximum number of iterations is reached without convergence, return the last estimate
    return x


# Test the function
print("Test 1:")
print(round(find_zero([1, 2], 0), 2))  # f(x) = 1 + 2x
print("Expected output: -0.5")

print("\nTest 2:")
print(round(find_zero([-6, 11, -6, 1], 0), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print("Expected output: 1.0")
```

Note that the `find_zero` function takes an additional argument `initial_guess`, which is the initial estimate for the root. This is necessary because the Newton-Raphson method can diverge if the initial guess is not close enough to the root. In the example above, we use 0 as the initial guess, but in practice, you may want to choose a different initial guess based on the specific problem at hand.