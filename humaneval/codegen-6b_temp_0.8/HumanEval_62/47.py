

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # find out the degree of polynomial
    n = len(xs)
    # this will be a list of lists
    result = [[] for i in range(n)]

    # calculate the derivative
    for i in range(n):
        # the derivative of degree i is the sum of all multiples of x^(n - i)
        # upto n - i
        result[i] = [xs[j] * (n - j) for j in range(n - i)]

    return result

