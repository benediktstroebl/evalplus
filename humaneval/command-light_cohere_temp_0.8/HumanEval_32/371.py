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
    find_zero finds x such that polynomial (x-xs[0]) has zero, or finds the highest non-zero coefficient.
    return (xs[0] == 0 and x==1) or return highest_nonzero_coeff and x<1
    """
    return (xs[0] == 0 and x==1) or return highest_nonzero_coeff and x<1

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2],
        [-6, 11, -6, 1],
        [0, 0, 0, 1, 2, 3]
    ]

    for case in test_cases:
        result = find_zero(case)
        assert result == (case[0] == 0 and x==1) or result == case[2]

    print("All tests passed!")
```