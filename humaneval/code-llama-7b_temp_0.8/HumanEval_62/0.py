

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # 1st case: xs is empty.
    if not xs:
        return xs

    # 2nd case: xs is of length 1.
    if len(xs) == 1:
        return []

    # 3rd case: xs is of length 2 or more.
    if len(xs) >= 2:
        derivative = []
        for i in range(len(xs) - 1):
            derivative.append(i * xs[i + 1])
        return derivative

