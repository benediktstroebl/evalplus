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

    assert len(xs) % 2 == 0, "Error: find_zero only takes list xs having even number of coefficients"
    assert all([coeff!= 0 for coeff in xs]), "Error: xs must contain non zero coefficient"
    if len(xs) == 2:
        return -xs[1] / xs[0]
    elif len(xs) == 4:
        return (xs[3] - xs[1]) / (xs[0] - xs[2])
    else:
        xs_ = [coeff for coeff in xs if coeff!= 0]
        xs_.sort(reverse=True)
        coeffs_ = [coeff for coeff in xs if coeff == 0]
        coeffs_.sort(reverse=True)
        xs_ = coeffs_ + xs_
        zero_ = find_zero(xs_[2:])
        for x in xs_[2:]:
            if x < zero_:
                return (x - 1) * zero_ + 1
        return (x - 1) * zero_
