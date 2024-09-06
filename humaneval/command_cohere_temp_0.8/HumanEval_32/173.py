Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, i.e. there may be multiple zeros.

    Algorithm:
    1. Create a list of pairs (coefficient, exponent) for all coefficients
       That is, if the list of coefficients is [1, -2, 3, 4], then the list of pairs is:
       [(1, 0), (-2, 1), (3, 2), (4, 3)]
    2. Sort this list of pairs -- this represents the polynomial in a different form
    3. Do an interval bisection search on the sorted list of pairs,
       starting at exponent = len(coefficients)
    """
    # Step 1
    n = len(coefficients)
    pairs = [(c, i) for i, c in enumerate(coefficients)]
    # Step 2
    pairs.sort()
    # Step 3
    def interval_bisect_search(target: float, l: float, r: float) -> float:
        while l <= r:
            m = (l + r) // 2
            if target >= m:
                l = m + 1
            else:
                r = m - 1
        return l

    def is_solution(x: float) -> bool:
        """
        Returns true if poly(x) = 0
        """
        return poly(coefficients, x) == 0.0

    # Start the bisect search from the monomiac with the largest exponent
    # This is the slowest-running term, so it is the most sensibly
    # to start the search here.
    exponent = n - 1
    while pairs:
        l = interval_bisect_search(exponent, 0, len(pairs))
        r = interval_bisect_search(exponent - 1, 0, len(pairs))
        pair = pairs[r]
        if is_solution(math.pow(pair[0], -1)) or is_solution(math.pow(pair[0], 1)):
            return math.pow(pair[0], -1)
        exponent = pairs[r][1]
        pairs = pairs[l:r + 1]
    # If we get to here, there is no solution
    return None
```

This script includes two functions: poly() evaluates the polynomial with the given coefficients at the given point x, and find_zero() finds the solution for the polynomial equaiton poly(x) = 0. The find_zero() function uses an algorithm that first represents the polynomial in a simplified form using a list of coefficient-exponent pairs, then performs an interval bisect search on the exponent values to find potential solutions for the polynomial equation. Finally, it checks if each potential solution is indeed a zero of the polynomial before returning the result.