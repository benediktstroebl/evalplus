```python
import math
def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("Input must be a list of length 2")
    x1, x2 = xs
    return x1 * x2 - x1 ** 2
``` 
This function implements a basic approach to solving the problem:
- It first checks if the length of the input list is not 2. If so, a ValueError is raised.
- It then computes the product of x1 and x2 and subtracts the square of x1^2. 

This function is self-contained and can be used to solve the problem of finding the zero of a polynomial of degree 2 with coefficients in the list xs.