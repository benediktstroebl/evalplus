def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.

    Args:
        xs (list): Coefficients of the polynomial in the format [xs[0], xs[1] * x, xs[2] * x^2, ...]

    Returns:
        list: Derivative of the polynomial in the same format [xs[0], xs[1] * x, xs[2] * x^2, ...]
    """

    derivative_xs = [0] * len(xs)
    x = 1

    for i in range(len(xs)):
        derivative_xs[i] = xs[i] * x
        x *= x

    return derivative_xs