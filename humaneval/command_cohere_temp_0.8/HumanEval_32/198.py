Here's a Python script that includes a function to solve the problem of finding a zero point of a polynomial:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check for curve with only one node
    if (len(xs) == 2 and xs[0] == 0 and xs[1] == 0):
        return 0

    # Check for vertical line
    if (len(xs) == 2 and xs[0] == 0):
        return xs[1]

    # Even number of coefficients
    if (len(xs) % 2 != 0):
        print("List xs should have even number of coefficients")
        return None

    # Take absolute values of xs
    xs = [abs(x) for x in xs]

    # Sort xs in descending order
    xs.sort(reverse=True)

    # Number of zeros could be 2*nds - 1, nds = floor((n+1)/2)
    nds = (len(xs)+1)//2
    zeros = []

    for i in range(nds):
        # calculating corresponding x for ith zero
        x = -xs[i] / (2*i + 1)
        zeros.append(x)

    # Here we are after all possible zeros,
    # now we find the only one find_zero function guarantees
    # It is the middle point between the smallest zero and the second smallest zero
    return (zeros[0] + zeros[1])/2

# Test cases
assert round(find_zero([1, 2]), 2) == -0.5, "One test case failed"
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0, "Second test case failed"
```

This script includes test cases to validate the `find_zero` function. Test cases are placed in the code to ensure the function behaves as expected. Adjust the test cases as needed based on your requirements. 

Let's break down the solutions I provided:
1. **poly(xs, x) function**:
   - This function takes two arguments: `xs`, which is a list of polynomial coefficients, and `x`, the point at which you want to evaluate the polynomial.
   - It uses a list comprehension and the `math.pow()` function to calculate the value of the polynomial at the given point `x`.
   - The term `xs[0] + xs[1] * x + xs[2] * x^2 + ...` corresponds to the usual summation formula for a polynomial.
2. **find_zero(xs) function**:
   - This function takes a list of polynomial coefficients `xs` and aims to find the value of `x` at which the polynomial evaluates to zero.
   - The function first checks if the list has only one element and it's zero, in which case it returns 0 (since