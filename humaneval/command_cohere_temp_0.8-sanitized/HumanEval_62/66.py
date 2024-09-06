def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in sums of powers of x.

    Args:
        xs (list): Coefficients of the polynomial, such as [3, 1, 2, 4, 5] for 3 + x + 2 x^2 + 4 x^3 + 5 x^4.

    Returns:
        List: Derivative of the polynomial, such as [1, 4, 12, 20] for the polynomial above.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * (x ** (len(xs) - 1 - i))
    return result