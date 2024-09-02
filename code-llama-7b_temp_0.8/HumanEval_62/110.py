

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # first let's write a derivative function which
    # can be applied to a polynomial.
    # The coefficients will be the derivative of the polynomial
    # represented by the input coefficients.
    # We can write a recursive equation for the derivative
    # for this equation.
    # The first coefficent in the output is the derivative
    # of the first coefficient in the input.
    # The next coefficent in the output is the difference
    # between the next coefficient in the input and the next coefficient
    # before it (the next coefficient in the input is the derivative of
    # the next coefficent before it)
    # The pattern is that the nth coefficent in the output is the derivative
    # of the nth coefficent before it.
    # so the base case is for the 0th coefficent
    # there is no 0th coefficent before it
    if not xs:
        return []
    # the recursive case is for the rest of the coefficents
    # we can assume the result will always be a list
    coeffs = [0] + xs
    # coeffs is now
    # [0, 3, 1, 2, 4, 5]
    # the first coefficient is always zero
    # the second coeffient is the first coefficent in the input list.
    # the third coefficent is the difference between the second coefficent in the input list
    # and the second coefficent before it
    # so on and so forth.
    coeffs = [coeffs[i+1] - coeffs[i] for i in range(len(xs))]
    return coeffs


