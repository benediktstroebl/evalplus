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
    assert max(xs) != 0  # better to assert this after the function call,
    # because it is more likely to fail.
    assert abs(max(xs)) < 1  # largest non-zero coefficient
    assert len(xs) % 2 == 0  # check this condition, since the function does not expect
    # multiple last coefficients,
    middle_index = len(xs) // 2
    left_sign = True if xs[0] < 0 else False
    for index in range(middle_index + 1):
        if left_sign is False:
            if xs[index] > 0:
                # for instance, if list is [1, 2, 3, 4, 5, -6, -4, -6]
                # then find_zero will return 6 since it is the second last non-zero
                # (index is 2, hence xs[index] is 6).
                return index - 1
            else:
                left_sign = True
        else:
            if xs[index] < 0:
                return index
            else:
                left_sign = False
    return False

