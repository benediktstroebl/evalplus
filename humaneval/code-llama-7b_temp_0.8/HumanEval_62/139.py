

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Hint: Start by using list comprehension to create an
    # initial list of values.
    # Then iterate across the list and compute the new values
    # Use the pattern to compute the next item in the new list.
    # Remember to discard the first item.
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return []
    ys = [0 for i in range(len(xs) - 1)]
    for i in range(1, len(xs)):
        ys[i - 1] = i * xs[i]
    return ys




