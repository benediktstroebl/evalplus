```python
import math

def find_poly_root(xs: list, x: float):
    """
    Determine polynomial roots.
    """
   xs: list, each element is a coefficient of the polynomial
    """
    return poly(xs, x) / math.pow(x)**(len(xs) - 1)

def test_find_poly_root():
    """
    Test if the find_poly_root function works as expected.
    """
    linear_combination = [1, 2, -3]
    assert find_poly_root(linear_combination, 2) == 0

if __name__ == "__main__":
    # Test other cases
    xs = [1, 2, -3]
    assert find_poly_root(xs, 2) == 0
    xs = [-6, 11, -6, 1]
    assert find_poly_root(xs, 2) == 0
```
The code defines a function `find_poly_root` that computes the roots of a polynomial using the `poly` function. The `test_find_poly_root` function tests the `find_poly_root` function by providing various test cases to ensure it works correctly. The `if __name__ == "__main__"` block tests the function in different scenarios.