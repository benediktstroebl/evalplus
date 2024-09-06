def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in its coefficients. """
    ans = [0] * (len(xs) - 1)
    for i in range(1, len(xs)):
        ans[i - 1] = xs[i] + xs[i - 1]
    return ans