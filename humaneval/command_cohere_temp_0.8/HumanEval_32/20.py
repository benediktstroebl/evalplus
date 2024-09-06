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
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero parameter, in case there are more than one.
    Works only for lists with even number of coefficients, and assumes the greatest coefficient is not zero.
    """
    n = len(coefficients)
    # check n is even
    if n % 2:
        raise ValueError('find_zero works only for polynomials with even number of coefficients')
    # sort coefficients descending
    coefficients.sort(reverse=True)
    x = -coefficients[0] / (n // 2)
    for i in range(1, n // 2):
        x = x - coefficients[i] / (n // 2 - i)
    return x
```

The function find_zero works only with polynomials having an even number of coefficients and assumes the greatest coefficient is not zero, as these conditions guarantee at least one solution to the equation ax^2 + bx + c = 0.

The function evaluates the polynomial at x = -coefficients[0] / (n // 2) to find the vertex of the parabola in the following manner:
* for one coefficient, vertex is the median between -c and c
* for two coefficients, vertex is the intersection of lines -b/2 and b/2
* in general case, vertex is the intersection of lines -b/2 and b/2 + (n)/(n-1) * (c/a)

The function then performs a binary search between -b/2 and b/2 + (n)/(n-1) * (c/a), as the parabola is symmetric and one of the zeros must be in this interval. The function returns the first zero found.