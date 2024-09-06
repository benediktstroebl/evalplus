Here's a Python script that includes a function to solve the problem:
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
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero as this
    guarantees a solution.
    """
    # make sure even number of coefficients, and largest is not zero
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "coefficients list must have even number of elements and largest coefficient is not zero"
    # assume x^n has coefficient cos(n*pi/2) = -1
    # we can divide polynomial by x^n and get one with odd number of coefficients
    # that starts with coefficient -1
    coefficients = [-1] + [coeff/math.pow(x, len(coefficients)) for x, coeff in enumerate(coefficients)]
    # now solve equation of form:
    # a_1*x^n + a_2*x^{n-1} + ... + a_n
    # use formula nroots from http://mathworld.wolfram.com/PolynomialRoots.html
    # x = (-a_1/(n*a_n))*((n-1)*cos(t)+sin(t))
    # where t = (2*pi/n)*k with k equal to 0 ... n-1
    # we use k=0 as it is the only value that gives a real solution
    # as value of sin(t) is always negative for k greater than 0
    roots = []
    for k in range(0, int(2 * math.pi / len(coefficients))):
        t = (2 * math.pi / len(coefficients)) * k
        roots.append((-coefficients[0]/(len(coefficients) * coefficients[-1])) *
                    ((len(coefficients) - 1) * math.cos(t) + math.sin(t)))
    return roots[0]
```

This script includes two functions: poly and find_zero. The poly function evaluates a polynomial given a list of coefficients and a point. The find_zero function finds the first root (where the polynomial equals zero) of a polynomial with an even number of coefficients. It assumes the largest coefficient is non-zero as this guarantees a solution.

The find_zero function converts the problem into a trigonometric equation with roots of the form: 
```
(-a_1/(n*a_n))*((n-1)*cos(t)+sin(t))
```
where t = (2*pi/n)*k with k equal to 0 ... n-1. We use k=0 as it is the only value that gives a real solution
as value of sin(t) is always negative for k greater than 0.
It then returns the first root it finds.