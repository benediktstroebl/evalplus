

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # Base case
    if not xs:
        return xs

    # Helper function to calculate derivative of a polynomial
    def derivative_helper(xs):
        result = []
        for i in range(1, len(xs)):
            result.append(xs[i - 1] * i)
        return result

    # Apply the derivative function recursively to the sublists
    result = []
    for i in range(len(xs)):
        sublist = xs[i:]
        result.append(derivative_helper(sublist))
    return result

