

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # Calculate length of polynomial
    n = len(xs)
    # Create a new array derivative with the length of polynomial - 1
    derivative = [0] * (n - 1)
    # Populate derivative array
    for i in range(n - 1):
        # For each coefficient of polynomial, append the next derivative
        # For e.g.
        # n = 3
        # xs = [1, 2, 3]
        # d = [1, 2]
        # n = 4
        # xs = [1, 2, 3, 4]
        # d = [2, 6]
        derivative[i] = xs[i + 1] * (i + 1)
    return derivative

