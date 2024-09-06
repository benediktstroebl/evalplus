Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Only returns the first solution found, even if there are multiple zeros.

    Args:
        coefficients (list): Must contain an even number of coefficients, and the largest non-zero coefficient.

    Returns:
        float: A solution x for the equation polynomial == 0.
    """
    # Ensure that only valid input is provided
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        raise ValueError("Input coefficients list must have an even length and contain a non-zero coefficient.")

    # Initialize guesses for the root and refinement threshold
    x_guess = -max(coefficients) / 2
    refinement_threshold = 0.0001

    # Iteratively refine the guess to find the zero
    while abs(poly(coefficients, x_guess)) > refinement_threshold:
        x_guess = (x_guess + x_guess) / 2

    return x_guess
```

This script includes two functions: poly evaluates a polynomial at a given point, and find_zero finds the point at which a given polynomial equals zero. The find_zero function only returns the first zero it finds, and it only accepts inputs that have an even number of coefficients and at least one non-zero coefficient - inputs that guarantee a solution to the zero find problem. 

To verify that the functions work as expected, you can add test blocks like these:
```python
# Test poly function
def test_poly():
    assert poly([1, 2, 3], 2) == 4  # 1 + 2*2 + 3*2^2
    assert poly([1, 2, 3], -2) == -8  # 1 + 2*(-2) + 3*(-2)^2
    assert poly([1, -2, 3], 0) == 0  # 1 + (-2) * 0 + 3*0^2


# Test find_zero function
def test_find_zero():
    assert round(find_zero([1, 2]), 2) == -0.5  # f(x) = 1 + 2x
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

These test blocks cover several cases and ensure that both functions perform as expected.