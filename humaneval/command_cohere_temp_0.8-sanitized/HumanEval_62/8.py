def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs where xs[0] is the constant term and xs[1:] are the coefficients of the linear and quadratic terms. """
    ans = [0] * (len(xs) - 1)
    for i in range(1, len(xs)):
        ans[i - 1] = xs[i] * (i + 1) - xs[i - 1]
    return ans