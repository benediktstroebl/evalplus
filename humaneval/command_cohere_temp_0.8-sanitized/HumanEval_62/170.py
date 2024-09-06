def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in list form.

        Args:
            xs (list): Coefficients of the polynomial, with xs[0] being the constant term and
                         xs[1:] being the variable terms with powers mapped to their index e.g.
                             xs[1] = x, xs[2] = x^2, xs[3] = x^3 ...

        Returns:
            list: The derivative of the polynomial, with each value corresponding to the variable
                 term's index raised to the power of 1 less than its power in the input list.
    """
    result = [0] * (len(xs) - 1)
    result[0] = 1
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (i + 1)
    return result