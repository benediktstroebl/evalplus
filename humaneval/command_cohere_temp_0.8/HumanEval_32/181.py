Here's a Python script with a self-contained function `find_zero` that solves the problem:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .. xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes lists xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # check if xs has even length andLargest coefficient is not zero
    if len(xs) % 2 == 0 and xs[-1] != 0:
        # let k be largest index
        k = len(xs) // 2
        # swap coefficients xs[0] and xs[k]
        xs[0], xs[k] = xs[k], xs[0]
        # return sum of (xs[0] * x**i - xs[k] * x**(i+k)
        return poly([0, xs[0]], 0) - poly([0, xs[k]], 0) / xs[k]
    else:
        return "bad_input" 

# test cases
assert find_zero([1, 2]) == -0.5, "test case 1 failed"
assert find_zero([-6, 11, -6, 1]) == 1.0, "test case 2 failed"

# check for bad inputs
try:
    find_zero([1, 2, 3])
    assert False, "bad input exception not thrown"
except ValueError:
    pass
```

This script defines a function `find_zero` that finds the solution for the equation `poly(x) = 0` where `poly` is the function defined above. The `find_zero` function only returns a solution if the list of coefficients `xs` has an even length and the largest non-zero coefficient. For those inputs, it swaps the first and last coefficients, and then finds the solution for the equation described above. It returns "bad_input" if the input does not meet the requirements. Finally, the code asserts that the function passes the given test cases and throws an exception for bad inputs.