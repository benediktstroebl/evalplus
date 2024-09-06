```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *x of x** i) for i, coeff in enumerate(xs)]

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    """
    return x
```

Below are the test cases that you can use to check if the above function correctly solves the problem and passes the test:

```python
test_cases = [
    ( [1, 2], 3),  # (x^2 + x)
    (-6, 11, -6, 1),  # (-x-1)^3
    (-9, -8, -9, -9),  # (-x^2 + x + 1)
    (-4, 4, -4, 4),  # (-x^2 + 2x + 1)
    # ...
]

for case in test_cases:
    x = float(case[0])
    xs = [float(i) for i in case[1]]
    result = find_zero(xs)
    assert x == result, "Error: did not find zero for {}.".format(case)
```

The test cases can be modified as needed, and you can add more test cases to ensure the function works correctly for different polynomial expressions.