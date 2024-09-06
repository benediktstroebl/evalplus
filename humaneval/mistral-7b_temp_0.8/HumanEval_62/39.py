

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    def add_coefficient(x, coeff):
        return coeff + xs[0] * xs[0] + xs[1] * xs[1] + xs[2] * xs[2] + xs[3] * xs[3] + xs[4] * xs[4]

    def subtract_coefficient(x, coeff):
        return coeff - xs[0] * xs[0] - xs[1] * xs[1] - xs[2] * xs[2] - xs[3] * xs[3] - xs[4] * xs[4]

    def multiply_coefficient(x, coeff):
        return coeff * xs[0] * xs[0] + coeff * xs[1] * xs[1] + coeff * xs[2] * xs[2] + coeff * xs[3] * xs[3] + coeff * xs[4] * xs[4]

    def divide_coefficient(x, coeff):
        return
