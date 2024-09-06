Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and with largest coefficient non-zero.
    """
    def find_ Solution(coefficients: list, target: float, interval_start: float, interval_end: float) -> float:
        """
        Returns x such that target == poly(x)
        """
        while True:
            mid = (interval_start + interval_end) / 2
            val = poly(coefficients, mid)
            if val < target:
                interval_start = mid
            elif val > target:
                interval_end = mid
            else:
                return mid

    if len(coefficients) % 2 == 0 and coefficients[0] != 0:
        # construct initial interval around midpoint of [-10,10]
        # very likely contains a root.
        return find_Solution(coefficients, 0, -10, 10)
    else:
        print("List of coefficients must have even length, and largest coefficient non zero.")
        return None
```

This script defines a polynomial evaluation function (`poly`) and a root-finding function (`find_zero`) that solves the given problem. The `find_zero` function specifically finds the first root of a polynomial with even coefficients, starting from an initial interval centered around `10`. 

The `find_zero` function demonstrates the following:
- It starts with an interval that is likely to contain a root, `[(-10,-10)`, `(10,10)]`.
- It uses a while loop and mid-point iteration to narrow down this interval.
- It returns the first root it finds, even if there are more. 

This is somewhat typical of root-finding functions that aim to find the first root quickly rather than all roots exactly. 

The `find_Solution` function is a helper used just for printing purposes in the docstring `find_zero`. 

This code provides a clear and efficient way to find the first root of a polynomial with even coefficients.