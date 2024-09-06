```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x,
    returns polynomial sum
    """
    return sum([coefficient * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Find polynomial zeroes
    """
    if len(xs) != len(set(xs)):
        raise ValueError("Input list has an odd number of coefficients.")
    for x in range(len(xs)):
        if xs[x] == 0:
            return x
    return 0
# Example usage:
xs = [1, 2, -5, -1]
x = float(find_zero(xs))
print("The solution is: ", x)
``` 
This script defines a function `poly` that evaluates a polynomial with a list of coefficients at a given point, and returns the polynomial sum. It also defines a function `find_zero` that finds the zeros of a polynomial with coefficients, and tests the function by providing an example usage.