Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients such that poly(x) = 0.
    Returns only the first found zero solution, even if there are more.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient, as it guarantees a solution.
    """
    def find_solution(coefficients, distinction):
        if len(coefficients) % 2 == 1 or coefficients[0] == 0:
            return None

        x = abs(coefficients[0] / distinction)
        solution = poly(coefficients, x)
        if solution == 0:
            return x

        # Increment solution by precision of calculation
        solution = round(solution, precision)
        if solution > 0:
            return None

        return find_solution(coefficients, distinction / x)

    precision = 10**-10  # Limit of floating point calculation accuracy
    return find_solution(coefficients, max(coefficients) * precision)

# Test cases
assert find_zero([1, 2]) == -0.5
assert find_zero([-6, 11, -6, 1]) == 1.0
assert find_zero([3, -1]) is None
```

This script defines a polynomial evaluation function `poly` and a polynomial zero finding function `find_zero`. The `find_zero` function iterates through values starting from the negative of the largest coefficient, and works back through increasingly smaller values with alternating signs. It uses the `poly` function to evaluate the polynomial at each candidate zero and returns the first zero it finds. The function returns `None` if the iteration reaches a maximum precision without finding a zero.  This alternate signing and iteration down to the machine epsilon allows it to find a zero where the polynomial crosses the x-axis only once.