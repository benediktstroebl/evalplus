Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution for the equation poly(x) = 0.
    Returns the value of x at which the polynomial evaluates to zero.

    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
    Returns:
        float: A float representing the value of x at which the polynomial evaluates to zero.
    """
    # Make sure that the list has even number of elements and the highest non zero element is the last.
    assert len(coefficients) % 2 == 0 and coefficients[-1] != 0, "List of coefficients should have even number of elements and the largest non-zero element at the last position."    
    # Let y be the wanted result. We have:
    # y*y == -coefficients[0] && y == 0
    # So y == 0 or y == sqrt(-coefficients[0])
    return 0 if coefficients[0] == 0 else math.sqrt(-coefficients[0])
```

This script defines a polynomial evaluation function `poly` and a polynomial zero finding function `find_zero`. The `find_zero` function checks for a valid input and returns 0 if the polynomial evaluates to 0. If the highest non-zero coefficient is negative, it returns a sqrt(-coefficient[0]). 

The functions are self-contained and do not rely on any external variables or functions, making them reusable and easy to test individually. 
The functions can be tested by calling them with example inputs: 
```python
round(poly([1, 2], 0.5), 2) # f(x) = 1 + 2x = 1 + 1 = 2 
round(poly([1, 2], 0.25), 2) # f(x) = 1 + 2x = 1 + 0.25 = 1.25
round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x = 0 at x = -0.5
round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 = 0 at x = 1
``` 

However, these tests are less reliable than a randomized comprehensive test, since they only check a small subset of inputs. 
A unittest would be a more reliable method of testing these functions, 
for example: 
 ```python
import unittest

class TestPolynomialFunctions(unittest.TestCase):
    def test_poly(self):
        self.assertEqual(poly([1, 2], 0.5), 2)
        self.assertEqual(poly([1, 2], 0.25), 1.25)
        with self.assertRaises(ValueError):
            poly([1, 2], -0.5)

    def test_find_