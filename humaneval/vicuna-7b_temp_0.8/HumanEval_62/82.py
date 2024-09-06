

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    n = len(xs)
    if n == 1:
        return xs[0]
    elif n == 2:
        return 2 * xs[0] + xs[1]
    else:
        ys = [0, 0, 0, 0]
        for i in range(n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    ys[i] += xs[k]
        return ys[n-1]
