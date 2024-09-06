```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x, returns sum of coefficients
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial is equal to zero
    """
    return math.floor(find_zero(xs))

def find_zero_test(xs):
    """
    test x value
    """
    return math.floor(find_zero(xs)) != find_zero(xs)

xs = [1, 2]
result = poly(xs)
assert result == 3, "poly not correct!"
assert find_zero_test(xs)
```
This script defines a function `poly` that computes the sum of the coefficients of a polynomial at a given point, and the function `find_zero` that finds the zero of a polynomial using the `find_zero` function from the math library. The function `find_zero_test` tests if the polynomial has a zero. 
The function then calls the `poly` function with the coefficients `[1,2]` and verifies that the result is equal to 3, and then asserts that the test passed. 
Finally, it calls the `find_zero_test` function with the coefficients `[1,2]` and asserts that the test also passes.