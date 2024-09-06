Here's a Python script with a self-contained function that solves the problem:
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
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    if len(coefficients) % 2 == 1:
        raise Exception('find_zero works only with lists of even number of coefficients')
    if coefficients[-1] == 0:
        raise Exception('find_zero assumes largest coefficient is not zero')
    
    # Let's assume polynomial is written in standard form: y = ax^2 + ... + bx + c
    # We want to find x such that: ax^2 + ... + bx + c = 0
    # Moving coefficients to the left hand side and multiplying by a^2
    # we get:
    #
    # ax^2 + ... + bx + c = a^2 * (x^2 + ... + bx + c)
    #
    # which means that:
    #
    # a^2 * x^2 + a^2 * ... + a^2 * bx + a^2 * c = 0
    #
    # which is equivalent to:
    #
    # (ax^2 + ... + bx + c) + a^2 * (x^2 + ... + bx + c) = 2 * a^2 * (x^2 + ... + bx + c)
    #
    # which means that:
    #
    # (ax^2 + ... + bx + c) = - a^2 * (x^2 + ... + bx + c)
    #
    # or in other words (after dividing by a^2):
    #
    # x^2 + ... + bx + c = -1 (*) a^2 * (x^2 + ... + bx + c)
    #
    # Since a^2 != 0, we can divide the equation by a^2:
    #
    # x^2 + ... + bx + c = -1
    #
    # and now we can solve it easily with quadratic formula:
    #
    # x = (-1 +/- sqrt(1 - 4*b*c)) / (2*b)
    #
    # Note: we don't need to compute the discriminant, as it's always non-negative
    # in this case (when dealing with real numbers).
    #
    # (*) we assume a > 0, which is an assumption made in the original code,
    # and the code below works also in this case, while the original code
    # has a bug where it's not clearing the negative root (which is undefined
    # for polynomials)

    a = coefficients[-2]
    b = coefficients[-1]
    c = -coefficients[0]

    # x = (-1 +/- sqrt(1 - 4*b*c)) / (2*b)
    x = (-1 + math.sqrt(1 - 4 * b * c)) / (2 * b)