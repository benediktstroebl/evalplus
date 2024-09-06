Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x**i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero solution, even if there are more.
    Works only for lists coefficients having an even number of coefficients
    and the largest non-zero coefficient, as it guarantees
    a solution.
    """
    n = len(coefficients)

    # Check for valid input
    if n % 2 == 1 or coefficients[n // 2] == 0:
        raise ValueError("Input coefficients list must have an even length"
                         " and contain a non-zero coefficient")

    # Calculate the zero boundary
    zero_boundary = [-coefficients[n // 2] / (n // 2 + 1)]

    # Iteratively find the zero solution using binary search
    for i in range(n // 2):
        # Calculate the boundary for this iteration
        boundary = [zero_boundary[0] - coefficients[i] / (i + 2)]
        # Binary search between boundaries
        x = bisect(boundary, 0)
        zero_boundary = [x] * 2

    return zero_boundary[0]

def bisect(a, x):
    """
    Returns index of x in a if x is in a, or nearest index to x if x is not in a.
    """
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
``` 

This script defines the poly function, which evaluates a polynomial given its coefficients and a variable value. The find_zero function, as an example of usage, finds the point at which poly evaluates to zero. It requires the list of coefficients to have an even number of items and for the largest non-zero coefficient to be present at the middle index for the guarantee of having a solution. It then uses a binary search algorithm to find the zero value. 

Note, that the find_zero function assumes that the list of coefficients is valid, i.e. has an even number of elements and the non-zero coefficient is in the middle. If the input does not fulfill these properties, a ValueError is raised.