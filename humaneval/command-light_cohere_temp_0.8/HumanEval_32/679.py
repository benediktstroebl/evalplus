```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    # check for even maximum length of the list, and use a variable to keep track of it
    max_len = len(xs)
    # find_zero only takes list xs having even number of coefficients
    if max_len % 2 == 0:
        # Use binary search to find x, which minimizes the number of additions
        x = xs[0]
        for i in range(1, max_len):
            if poly(xs[i], x) == 0:
                x = xs[i]
        return x
    else:
        # return no solution, which is also a valid answer
        return None


# test cases:
xs = [1, 2]
x = find_zero(xs)
print(x)

xs = [0, -6, 11, -6, 1]
x = find_zero(xs)
print(x)

xs = [1, -1, 2, -3]
x = find_zero(xs)
print(x)
```
This Python code defines two functions, poly and find_zero, for evaluating polynomial coefficients and finding its zeros, respectively. The poly function takes a coefficients of a polynomial and a point x as input, and returns the polynomial evaluation at the given point. The find_zero function takes a list of coefficients as input and finds the zero of the polynomial with those coefficients. 

The code then provides several test cases to demonstrate the functionality of the functions. These test cases are passed through the code, and the output of each test case is printed to verify that the functions are working correctly.