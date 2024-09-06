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
    Finds a solution x for polynomial coefficients polynomial such that poly(x) = 0.
    Returns only one solution, even in the presence of multiple zeros.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient.
    """
    # make sure list has even number of coefficients and
    # contains a non-zero coefficient
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return "coefficients list must have even length, and contain a non-zero coefficient"
    # make sure the leading non-zero coefficient is twice the coefficient
    # that follows it
    if coefficients[-2] == 0:
        return "List must have a non-zero coefficient before the leading coefficient."
    leading_coef, next_coef = coefficients[-1], coefficients[-2]
    multiple = leading_coef / next_coef
    if not multiple.is_integer():
        return "Leading coefficient must be divisible by the second largest coefficient"
    return next_coef * multiple - leading_coef
```

#### Testing:
```python
import unittest

class TestPolyFunction(unittest.TestCase):
    def test_ evaluates_first_term(self):
        self.assertEqual(poly([1, 2, 3], 2), 1+4)

    def test_ evaluates_multiple_terms(self):
        self.assertEqual(poly([1, 2, 3], 3), 1 + 6 + 12)

    def test_ evaluates_with_negative_terms(self):
        self.assertEqual(poly([-2, 3, -4, 5], 4), -2 + 12 +-16 + 20)

    def test_ handles_zero_as_coefficient(self):
        self.assertEqual(poly([3, 0, 4], 5), 3 + 0 + 20)

    def test_ handles_single_term(self):
        self.assertEqual(poly([7], 7), 7)

class TestFindZero(unittest.TestCase):
    def test_ handles_leading_coef(self):
        self.assertEqual(find_zero([5, 10, 5]), -10)

    def test_ handles_leading_coef_with_negative(self):
        self.assertEqual(find_zero([-3, -10, 5]), 2)

    def test_ handles_leading_coef_with_zero(self):
        self.assertEqual(find_zero([0, -10, 10]), 0)

    def test_ handles_second_coef_zero(self):
        self.assertEqual(find_zero([-5, 0, 15]), 0)

    def test_ non_integer_coef(self):
        self.assertEqual(find_zero([-6, 11, -6, 1]), 1)

    def test_ no_solution_for_negative_second_coef(self):
        self.assertEqual(find_zero([5, -10, 5]), "Leading coefficient must be divisible by the second largest coefficient")

    def test_ no_solution_for_leading