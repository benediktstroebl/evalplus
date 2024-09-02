

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # let p(x) = xs[0] + xs[1]*x + xs[2]*x^2 + .... + xs[n]*x^n
    # Return derivative of this polynomial in the same form.
    n = len(xs)
    if n == 1:
        return [0]
    elif n == 2:
        return [xs[1]]
    else:
        return [xs[1] + 2*xs[2]*xs[0] + xs[3]*2*xs[0] + xs[4]*3*xs[1] +
                xs[5]*4*xs[2] + xs[6]*5*xs[3] + xs[7]*6*xs[4] + xs[8]*7*xs[5] +
                xs[9]*8*xs[6]]
