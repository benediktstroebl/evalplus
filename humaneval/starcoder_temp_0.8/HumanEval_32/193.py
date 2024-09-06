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
    assert len(xs) % 2 == 0, "find_zero only takes list xs having even number of coefficients"
    assert max(xs) > 0, "find_zero only takes list xs having largest non zero coefficient"

    # the number of coefficients
    k = len(xs) // 2

    # Find the initial point in the range of the largest non zero coefficient
    for i in range(k):
        if xs[i]!= 0:
            break

    # Find the root using Brent's method
    root = i
    max_iter = 10000000
    eps = 0.00000001
    prev = i
    while max_iter > 0:
        # Find interval
        if prev > 0:
            left = prev
        else:
            left = 0

        if prev + k < len(xs):
            right = prev + k
        else:
            right = len(xs) - 1

        # Find the mid point
        mid = (left + right) // 2

        # Check if the mid point is a root
        if abs(poly(xs, mid)) < eps:
            root = mid
            break

        # Check if the left side of the mid point is a root
        if abs(poly(xs, left)) < eps:
            root = left
            break

        # Check if the right side of the mid point is a root
        if abs(poly(xs, right)) < eps:
            root = right
            break

        # Check if the left side of the mid point is a minimum
        if poly(xs, left) * poly(xs, mid) < 0:
            right = mid
        # Check if the right side of the mid point is a minimum
        elif poly(xs, mid) * poly(xs, right) < 0:
            left = mid
        else:
            print("There is no minimum here")
            break

        # Decrease the maximum number of iterations
        max_iter -= 1
        prev = mid

    return root

