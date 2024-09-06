```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes the polynomial equal to 0, returns only x, and does not modify xs.
    """
    largest_nonzero = float('-inf')
    for x in range(math.inf):
        if xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[len(xs)-1] * x**len == 0:
            largest_nonzero = max(largest_nonzero, x)
    return largest_nonzero


# Test cases
xs = [1, 2]
xs = [-6, 11, -6, 1]
test_case = find_zero(xs)
print("Test case:", test_case)
xs = [1, -1, 2, -3]
test_case = find_zero(xs)
print("Test case:", test_case)
xs = [2, -3, -8, 4]
test_case = find_zero(xs)
print("Test case:", test_case)
``` 
The output of the script will be the value of `find_zero` corresponding to the test cases provided. The test cases in the script are designed to test the `find_zero` function, which is a function that finds the roots of a polynomial equation.