```python
import math

def find_zero(xs):
    """
    Find x-values that make polynomial equal to 0.
    xs = [i for i, coeff in enumerate(xs) if coeff != 0]
    return xs

def test(xs, y):
    """
    Test whether given list xs can produce polynomial y=0
    test = False
    for i, coeff in enumerate(xs):
        if coeff == 0:
            test = True
            break
    return test

def poly(xs: list, y: float):
    """
    Evaluates polynomial with coefficients xs at point y
    return xs.poly(y)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

xs = [1, 2]
y = find_zero(xs)
print(y) # [1, 2]
print(test(xs, y))  # True
``` 
This solution uses a function test to check whether a polynomial given by two lists xs and y can be evaluated to y=0. The function test then calls test with the lists xs and y, and returns True if the test passes.