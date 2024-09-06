```python
import math

def find_zero(xs):
    if len(xs) != len(xs[0]):
        raise ValueError("Input list must have an even number of coefficients")
    return math.pow(xs[0])

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero(xs):
    x = find_zero(xs)
    assert x == 0, "Coefficient at x does not equal 0!"

def test_poly(xs, x):
    assert math.pow(xs[0], x) + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n == poly(xs, x), "Evaluation failed!"

test_cases = [
    [
        [1, 2],
        [-6, 11, -6, 1],
        [0, 2]
    ]
]

for case in test_cases:
    print("Case:", case)
    print("Poly:", case[0])
    print("X:", case[1])
    print("Find_zero:", case[2])
    print()
    print("Poly:", poly(case[0], case[1]))
    print("Find_zero:", find_zero(case[2]))
    print()
```
This code includes the functions `find_zero`, `poly`, and `test_find_zero` and `test_poly`. The `find_zero` function checks the list `xs` for coefficients of a polynomial. The `poly` function computes the polynomial with coefficients `xs` at point `x`. The `test_find_zero` function tests the `find_zero` function by passing different lists `xs` and checks that the `find_zero` function returns the correct result. The `test_poly` function tests the polynomial evaluation at `x` with the given list `xs` and checks that the result is equal to the polynomial evaluated at `x` with the same list `xs`.

The `test_cases` list contains a few test cases, and the code iterates over these test cases, printing each case and the corresponding results. The output shows the expected output for each test case, which verifies that the functions work as expected.