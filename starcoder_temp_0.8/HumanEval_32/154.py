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

    def sign_changes(xs: list):
        """
        Sign changes in a list of numbers.
        """
        return sum([1 for i in range(1, len(xs)) if xs[i - 1] * xs[i] < 0])

    def rec_find_zero(xs: list, r: list):
        """
        Recursively finds zero point of a polynomial
        Args:
            xs: coefficients of a polynomial, zero point is searched in this
                polynomial.
            r: candidate zero point list.
        Returns:
            r: zero point list found after searching xs.
        """
        k = sign_changes(xs)
        if k == 0:
            # xs is a constant function, one of its coefficients is a root.
            r.append(xs[0])
            return r
        elif k == 1:
            # xs has at least one root, r contains at least one candidate.
            xs_k = xs[len(xs) - k]
            ys_k = poly(xs, xs_k)
            if ys_k == 0:
                # xs is a constant function, one of its coefficients is a root.
                r.append(xs_k)
                return r
            else:
                # xs has at least one root, r contains at least one candidate.
                return rec_find_zero(
                    [xs_k, 1],
                    [
                        x_k
                        for x_k in r
                        if poly([xs_k, 1], x_k) * poly(xs, x_k) < 0
                    ],
                )
        else:
            # xs has two or more roots and none of them is in r.
            return r

    return rec_find_zero(xs, [])[0]

