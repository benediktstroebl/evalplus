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
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient, as it guarantees
    a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        raise ValueError("List coefficients should have even length and largest non-zero coefficient.")

    x = -coefficients[0] / coefficients[-1]
    temp = [x]
    for i in range(1, len(coefficients) // 2 + 1):
        x = x - coefficients[i] / coefficients[-(i + 1)]
        temp.append(x)
    
    # so that solution is within [0, 1]
    return min(temp)
```

The function find_zero only returns the first zero it finds, even if there are multiple solutions. It also only works for polynomials with an even number of coefficients and the largest non-zero coefficient, as these polynomials will have a zero. If the input list does not meet these requirements, the function raises a ValueError. 

To see if the function works, let's run some tests:
```python
test_cases = [
    ([1, 2], -0.5),
    ([-6, 11, -6, 1], 1.0),
    ([1, 2, 3], 1.0),
    ([1, -2], 0.0),
]

for coefficients, expected in test_cases:
    try:
        actual = find_zero(coefficients)
        assert abs(actual - expected) < 1e-6
    except ValueError as e:
        assert str(e) == 'List coefficients should have even length and largest non-zero coefficient.'
``` 

This tests the function with different polynomial coefficients, expecting it to find the correct zero point.