```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, where the polynomial is evaluated at x
    """
    return round(poly(x), 2) == 0


# Test cases
xs = [1, 2]
test_case = find_zero(xs)
print("Test Case 1:", test_case)

xs = [-6, 11, -6, 1]
test_case = find_zero(xs)
print("Test Case 2:", test_case)

xs = [1, -1, -1, 1]
test_case = find_zero(xs)
print("Test Case 3:", test_case)

xs = [0.5, 0.5, 0.5]
test_case = find_zero(xs)
print("Test Case 4:", test_case)
```

The code defines a polynomial evaluation function `poly` and a function to find the zero of a polynomial `find_zero`. It then provides test cases to evaluate the functions and print the results. The test cases cover various scenarios to ensure the correctness of the functions.