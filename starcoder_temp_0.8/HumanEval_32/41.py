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
    if len(xs) % 2 == 0:
        # xs has even number of coefficients
        # and largest coefficient is non zero
        # which guarantees a solution
        # get middle index of list
        mid_index = len(xs) // 2
        # get middle coefficient
        mid_coeff = xs[mid_index]
        # get sub list with the middle coefficient removed
        sublist = xs[0:mid_index] + xs[mid_index + 1 :]
        # sub list is used to find zero point of
        # polynomial with smaller coefficients
        sub_zero = find_zero(sublist)
        # find zero point of polynomial with smaller coefficients
        # multiply mid coefficient by the zero point
        # of polynomial with smaller coefficients
        # this is the zero point of polynomial with
        # smaller coefficients
        zero = mid_coeff * sub_zero * sub_zero + sub_zero
        return zero
    else:
        # if list xs has odd number of coefficients
        # find zero point of polynomial with smaller coefficients
        # and multiply last coefficient with it.
        zero = find_zero(xs[0:-1])
        # find zero point of polynomial with smaller coefficients
        # multiply mid coefficient by the zero point
        # of polynomial with smaller coefficients
        # this is the zero point of polynomial with
        # smaller coefficients
        zero = xs[-1] * zero * zero + zero
        return zero

