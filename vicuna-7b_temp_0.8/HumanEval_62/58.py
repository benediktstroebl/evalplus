

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize derivative list
    derivative_list = [0] * len(xs)

    # Compute derivative using recursion
    for i in range(len(xs) - 1):
        derivative_list[i] = xs[i + 1] * derivative_list[i + 1]

    return derivative_list