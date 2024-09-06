```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that polynomial f(x) = 0,
    find_zero returns only zero point, even if there are many solutions.
    """
    result = -0
    for x in range(-10, 10):
        if f(x) == 0:
            result = x
    return result

# Test cases
test_cases = [
    [1, 2],
    [-6, 11, -6, 1],
    [2, 3, 0, 1]
]
test_cases_str = [f"{i} {j}" for i, j in test_cases]

print("Test cases: ", end="")
for i, test in enumerate(test_cases):
    print(f"{i+1}: {test}")

print(" =======================================")

for i, test in enumerate(test_cases):
    print(f"Evaluating polynomial with coefficients {test} at x = 0...")
    print(f"Result: {poly(test, 0)}")

print(" =======================================")

for i, test in enumerate(test_cases):
    print(f"Zero point of polynomial {test}: {find_zero(test)}")
```
This Python script defines a function `poly` that evaluates a polynomial with given coefficients at a given point `x`. The `find_zero` function is then used to find the zero point of the polynomial.

The script then provides a series of test cases, each consisting of a list of coefficients and a target point, and evaluates the polynomial at the target point using the `poly` function. The script also finds the the zero point of the polynomial using the `find_zero` function. 

Finally, the script prints out the test cases and their results.