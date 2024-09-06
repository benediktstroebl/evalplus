

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # x^n = x * x^(n-1)
    # d/dx(x^n) = (n-1) * x^(n-2) + 1 * x^(n-1)
    # d/dx(x^n) = n * x^(n-2) + x^(n-1)
    # d/dx(x^n) = x^(n-1) * (n + 1)

    result = [0] * len(xs)

    for i in range(len(xs)):
        # Derivative of x^n
        result[i] = xs[i] * (i + 1)

    return result
