

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def poly(x, coefs):
        return sum(coef * x ** i for i, coef in enumerate(coefs))
    def derivative(coefs):
        next_coefs = []
        for i in range(len(coefs) - 1):
            next_coefs.append(coefs[i + 1])
            next_coefs.append(coefs[i] * (i + 1))
        return next_coefs
    return derivative(xs)
