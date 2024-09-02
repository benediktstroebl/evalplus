

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    new_xs = [0]
    # TODO
    # new_xs is the list we are looking for
    # first element of new_xs is the first element of xs
    # then we have xs[0]
    # then we have xs[1] + 2 * xs[0]
    # then we have xs[2] + 3 * xs[1] + 3 * xs[0]
    # then we have xs[3] + 4 * xs[2] + 6 * xs[1] + 4 * xs[0]
    # then we have xs[4] + 5 * xs[3] + 10 * xs[2] + 10 * xs[1] + 5 * xs[0]
    for i in range(len(xs)):
        if i == 0:
            new_xs[i] = xs[i]
        elif i == 1:
            new_xs[i] = xs[i] + 2 * xs[i-1]
       
