```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert all(xs[i] > 0 for i, x in enumerate(xs))
    return xs[0]

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

if __name__ == "__main__":
    # Test the function
    xs = [1, 2]
    assert find_zero(xs) == 0.5
    xs = [-6, 11, -6, 1]
    assert find_zero(xs) == -6.5
    xs = [3, 4, 5]
    assert find_zero(xs) == 5.0
    xs = [3, -4, 5]
    assert find_zero(xs) == -4.0
    ```