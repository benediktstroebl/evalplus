```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes the polynomial equal to zero
    find_zero returns x that satisfies this equation
    """
    # Ensure even number of coefficients
    assert len(xs) % 2 == 0
    x = float('inf')
    for x in range(0, min(10, len(xs) // 2 + 2)):
        polynomial = xs[0] + xs[1] * x + xs[1] * x**2 + xs[2] * x**3 + xs[3] * x**4 + ...
        # x == 0 if polynomial is equal to 0
        if polynomial == 0:
            return x
    return float('inf')  # No solution

# Test cases
xs = [1, 2]
test_find_zero = find_zero(xs)
print("Test 1:", test_find_zero)
assert math.equal(poly(xs, test_find_zero)) == 0
xs = [6, 11, -6, 1]
test_find_zero = find_zero(xs)
print("Test 2:", test_find_zero)
assert math.equal(poly(xs, test_find_zero)) == 0
xs = [-6, 11, -6, 1]
test_find_zero = find_zero(xs)
print("Test 3:", test_find_zero)
assert math.equal(poly(xs, test_find_zero)) == 0
xs = [1, -2, 3, -4, 5, 6, 7, -1, -3]
test_find_zero = find_zero(xs)
print("Test 4:", test_find_zero)
assert math.equal(poly(xs, test_find_zero)) == 0
```
The provided Python script defines a self-contained function `find_zero` that finds the zeros of a polynomial. The `poly` function is defined to evaluate a polynomial at a given point `x` and returns the polynomial's value at `x`. The script then provides a set of test cases with various polynomial coefficients and `x` values. The `find_zero` function is used to find the zeros of the polynomial corresponding to each test case. The output will show the expected zeros based on the polynomial's coefficients.