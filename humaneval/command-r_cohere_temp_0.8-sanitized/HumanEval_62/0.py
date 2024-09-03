def derivative(xs):
    """ Compute derivative of the polynomial represented by xs.
    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative polynomial.
    """
    ds = [0] * len(xs)
    for i in range(1, len(xs)):
        ds[i - 1] = i * xs[i]

    return ds