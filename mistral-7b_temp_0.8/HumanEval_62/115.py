

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def helper(xs: list, n: int) -> list:
        if len(xs) < n:
            return []
        if n == 0:
            return xs
        next_derivative = helper(xs, n - 1)
        # Add previous number to next derivative
        # i.e. 3x^2 --> 6x, 2x^3 --> 6x^2
        # This is accomplished by multiplying the previous
        # element by the new element
        # i.e. 3 * 2 = 6
        return [(next_derivative[i] * xs[i] + xs[i+1]) for i in range(len(next_derivative))]

    return helper(xs, 1)

