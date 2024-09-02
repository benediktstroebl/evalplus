

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Copy the list to avoid modifying the input
    xs = list(xs)
    # Get the degree of the polynomial
    degree = len(xs)
    # Get the coefficients of the derivative
    coeffs = [0] * (degree + 1)
    for i in range(degree):
        coeffs[i] = (xs[i] * (degree - i) // 2)
    # Get the derivative as a list
    return [coeffs[degree - j] for j in range(degree)]