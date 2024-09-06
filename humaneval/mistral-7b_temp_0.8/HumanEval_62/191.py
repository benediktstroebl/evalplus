

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Your code here
    xs_copy = xs.copy()
    xs_copy.insert(0, 0)
    xs_copy.insert(1, 0)
    for i in range(len(xs_copy)):
        xs_copy[i] *= i
    xs_copy.insert(0, 1)
    xs_copy.insert(1, 0)
    for i in range(len(xs_copy)):
        xs_copy[i] /= xs_copy[i - 1]
    return xs_copy[1:]
