

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    coeffs = [xs[i] for i in range(1, len(xs))]
    prod = 1
    for i in range(1, len(coeffs)):
        prod *= coeffs[i]
    return [product(range(len(coeffs)), start=i, end=j) for i in range(1, len(coeffs)) for j in range(len(coeffs))]
