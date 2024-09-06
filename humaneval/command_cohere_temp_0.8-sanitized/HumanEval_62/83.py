def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.

    Polynomial is in the form: xs[0] + xs[1] * x + xs[2] * x^2 + ...

    Returns: A list of coefficients of the derivative, in the same form.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    poly = 0
    for i in range(len(xs)):
        temp = 1
        for j in range(i+1, len(xs)):
            temp *= j
        poly += xs[i] * temp
    return [xs[i] * temp for i, temp in enumerate(poly)]