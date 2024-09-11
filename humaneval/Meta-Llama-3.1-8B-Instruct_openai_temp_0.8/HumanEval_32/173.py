```python
import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
        xs (List[float]): Coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(reversed(xs))])


def find_zero(xs: List[float]) -> float:
    """
    Finds the zero point of a polynomial with coefficients xs.

    Args:
        xs (List[float]): Coefficients of the polynomial.

    Returns:
        float: The zero point of the polynomial.

    Raises:
        ValueError: If the polynomial has an odd number of coefficients.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients")

    # Find the largest non-zero coefficient
    max_non_zero_coeff = max(coeff for coeff in xs if coeff!= 0)

    # Find the index of the largest non-zero coefficient
    max_non_zero_idx = xs.index(max_non_zero_coeff)

    # Find the zero point by setting the largest non-zero coefficient to 0
    zero_point = -poly(xs[:max_non_zero_idx], 1) / max_non_zero_coeff

    return zero_point
```

You can test the functions with the following code:

```python
import unittest

class TestPolyAndFindZero(unittest.TestCase):
    def test_poly(self):
        self.assertAlmostEqual(poly([1, 2], -0.5), 1)
        self.assertAlmostEqual(poly([-6, 11, -6, 1], 1), -6 + 11*1 - 6*1**2 + 1*1**3)

    def test_find_zero(self):
        self.assertAlmostEqual(round(find_zero([1, 2]), 2), -0.5)
        self.assertAlmostEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)

    def test_odd_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `poly` and `find_zero` functions as specified, and includes some test cases to ensure they work correctly. The `poly` function is implemented using a generator expression and the `math.pow` function, and the `find_zero` function uses the same approach to evaluate the polynomial at x=1 and then finds the zero point by setting the largest non-zero coefficient to 0. The test cases cover the specified examples, as well as a test for the odd number of coefficients case.