

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    xs = np.array(xs)
    xs_derivative = np.zeros(xs.shape)
    for i in range(xs.shape[0]):
        if i == 0:
            xs_derivative[i] = xs[i+1] - xs[i]
        else:
            xs_derivative[i] = xs[i] + xs[i-1]
    return xs_deriv
