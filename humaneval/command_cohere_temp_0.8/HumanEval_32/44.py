Here's a Python script with a self-contained function `find_zero` that solves the problem:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Returns only the first solution x, even if there are multiple zeros.
    Works only for lists xs with an even number of coefficients, and the largest non-zero coefficient.
    """
    if len(xs) % 2 == 1 or max(xs) == 0:
        return "Invalid input. Must provide an even number of coefficients and a largest non-zero coefficient."

    # Arrange coefficients in descending order and flip sign
    xs = list(reversed(sorted(xs, reverse=True)))
    x = xs.pop()
    while len(xs) > 0: 
        x = x / xs.pop()
    return x
```

The function assumes that the input list `xs` has an even number of elements and that all coefficients are integers, as per the problem statement. It also assumes that the input list has been normalized to contain the largest non-zero coefficient first.

The function works by constructing the polynomial numerator by numerator, taking the inverse of the leading coefficient, and dividing it from the polynomial, ad infinitum. This is, essentially, synthetic division, except it's done iteratively in reverse.

Here's a test suite to validate the function:
```python
import math
import unittest

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """

class TestFindZero(unittest.TestCase):
    def test_find_zero_valid(self):
        self.assertEqual(find_zero([1, 2]), -0.5)
        self.assertEqual(find_zero([-6, 11, -6, 1]), 1.0)
        self.assertEqual(find_zero([0, -1, -1, 0, -1, 2, -3, 2]), 1.0)
        self.assertEqual(find_zero([-1, -1, -1, -1, -1, -1, -1,