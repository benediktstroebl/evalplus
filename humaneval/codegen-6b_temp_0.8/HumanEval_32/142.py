import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 == 1:
        raise ValueError(
            "There should be an even number of coefficients for find_zero.")
    if len(xs) > 1:
        if min(xs) == 0:
            return True
        if max(xs) == 0:
            return min(xs)
    if xs[-1] == 0:
        return True
    coeff, left, right = [], [], []
    for i in range(len(xs)):
        if xs[i] != 0:
            coeff.append(xs[i])
            left.append(i)
        else:
            right.append(i)
    if len(left) > len(right):
        left, right = right, left
    for i in range(len(left) - 1):
        if coeff[left[i]] * coeff[left[i + 1]] > 0:
            left[i], left[i + 1] = left[i + 1], left[i]
    for i in range(len(right) - 1):
        if coeff[right[i]] * coeff[right[i + 1]] < 0:
            right[i], right[i + 1] = right[i + 1], right[i]
    left.extend(right)
    left.sort()
    if poly(coeff, 1) == 0:
        return 1
    if len(left) % 2 == 1:
        if poly(coeff, -left[len(left) // 2 - 1]) == 0:
            return -left[len(left) // 2 - 1]
        else:
            return -left[len(left) // 2]
    left = sum(left) / len(left)
    if poly(coeff, -left) == 0:
        return -left
    return round(left, 2)

