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
    find_zero find x such that poly(x) = 0
    find_zero returns x and xs[0] such that xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n = 0

    """

    def test_poly(xs: list, x: float):
        """
        Test if polynomial with coefficients xs evaluated at x equal 0.
        """
        test_poly(xs, x) == 0
        """
        return True if xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n == 0 else False

    def test_find_zero(xs: list, x: float):
        """
        Test if find_zero returned x when given xs.
        """
        test_find_zero(xs) == x
        """
        return True if xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n == 0 else False

    test_poly([1, 2], 2)
    test_find_zero([1, 2], 2)  # Should return True

    test_poly([-6, 11, -6, 1], 2)
    test_find_zero([-6, 11, -6, 1], 2)  # Should return True

    test_poly([1, 2, -3], 2)
    test_find_zero([1, 2, -3], 2)  # Should return False

The script defines functions for evaluating polynomials, finding zeros, and testing the correctness of polynomial evaluation and finding zeros. The test functions demonstrate the test cases, showing the expected behavior of the functions.