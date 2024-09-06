

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Copy xs to new list
    ys = []
    # Find the first nonzero element
    for x in xs:
        if x!= 0:
            break
        ys.append(0)
    # Compute the derivative
    for i in range(1, len(xs)):
        ys.append(i * xs[i])
    return ys

