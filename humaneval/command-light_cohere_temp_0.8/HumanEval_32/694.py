```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many
    and none are real.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    return math.floor(find_zero(xs, 2))  # using math.floor to round to int
```

def test_find_zero(xs: list):
    """
    Test case 1: find zero for f(x) = 4x^3 - 3x^2 + 4
    test_find_zero( [4, -3, 4])
    assert find_zero([4, -3, 4]) == 2.0
    """
   
    Test case 2: find zero for f(x) = 4x + 2
    test_find_zero( [4, 2])
    assert find_zero([4, 2]) == 2.0
    """
    test case 3: find zero for f(x) = x - 2
    test_find_zero( [1, -2])
    assert find_zero([1, -2]) == -1.0
```

This Python script defines a function **poly** to evaluate a polynomial at a given point **x**, and a function **find_zero** to find the zero of a polynomial. The **test_find_zero** function provides a set of test cases to verify the correctness of the **find_zero** function.