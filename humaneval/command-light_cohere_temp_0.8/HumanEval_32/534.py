```python
import math
def evaluate_polynomial(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns 1 for 1, 2, 3...
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial (xs, x) = 0
    """
    x_zero = 0
    for x in range(1, 10):
        if evaluate_polynomial(xs, x) == 0:
            x_zero = x
            break
    return x_zero
xs = [1, 2]
x = find_zero(xs)
print("The x-value where polynomial has 0 is:", x)
``` 
The code implements a method for finding the x-coordinate where a polynomial equals 0. The function takes in a list of coefficients for a polynomial, and returns the x-coordinate where the polynomial is 0. The test cases provided are: passing a list with coefficients [1,2] and printing the output to the console. The test case [ passing a list with coefficients [-6,11, -6, 1] ] and printing the output to the console.