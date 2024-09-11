```python
import math
import cmath

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero point x of a polynomial defined by xs.
    xs is a list of coefficients, where the first coefficient is the constant term.
    xs must have an even number of elements.
    The function returns the first found zero point.
    """
    
    # Check if xs has an even number of coefficients
    if len(xs) % 2 == 1:
        raise ValueError("xs must have an even number of coefficients")

    # Ignore zero coefficients
    xs = [x for x in xs if x!= 0]

    # Find the largest non-zero coefficient
    max_coeff = max(abs(x) for x in xs)

    # Initialize x with the value that yields the largest non-zero coefficient
    x = -xs[0] / xs[1] if len(xs) > 1 else float('inf')

    # Use Newton-Raphson method to find a zero point
    while True:
        x_new = x - poly(xs, x) / poly([i * x**(len(xs) - i - 1) for i in range(len(xs))], x)
        if abs(x_new - x) < 1e-12:
            break
        x = x_new

    return x

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
Note: The above code uses a simple implementation of the Newton-Raphson method to find a zero point of the polynomial. However, this method may not be reliable for all polynomials, especially those with complex roots or multiple roots. For more robust results, consider using a library like `numpy.roots`. 

Also note that the `poly` function uses `math.pow(x, i)` which can be slow for large values of `x`. A more efficient approach would be to use `x**i` directly. 

The `find_zero` function also ignores zero coefficients from the list. This is because a coefficient of zero does not contribute to the value of the polynomial. 

Finally, the function raises a `ValueError` if the input list does not have an even number of elements. This is because the Newton-Raphson method requires the polynomial to be of degree at least 2. 

The test cases at the end of the code demonstrate the usage of the `find_zero` function with two different polynomials.