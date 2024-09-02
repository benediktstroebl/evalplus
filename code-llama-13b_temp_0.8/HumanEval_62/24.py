

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # Tip: try to express the derivative in terms of the original polynomial.
    #
    # Note that a polynomial can be expressed as a sum of terms
    # P(x) = a_0 + a_1*x + ... + a_n*x^n
    #
    # For example, the polynomial P(x) = 3 + 2x - 6x^2 + 7x^4 can be
    # expressed as a list [3, 2, -6, 0, 7].

    # TODO: add your code here

    #raise NotImplementedError

    # if xs[0] == 0:
    #     return derivative(xs[1:])
    # else:
    #     return [k * xs[0] for k in range(1, len(xs))] + derivative(xs[1:])

    return [k * xs[0] for k in range(1, len(xs))] + derivative(xs[1:]) if xs[0] != 0 else derivative(xs[1:])



