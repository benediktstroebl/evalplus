

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) <= 1:
        return xs

    xs_without_first_element = xs[1:]
    new_coeff = [0] + xs

    for i in range(len(xs_without_first_element) + 1):
        new_coeff[i + 1] = new_coeff[i] * i

    return [sum(xs_without_first_element), *new_coeff]

