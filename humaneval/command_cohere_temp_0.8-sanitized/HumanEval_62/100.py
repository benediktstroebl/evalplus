def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    ans = [0]*(len(xs)-1)
    num = 1
    for i in range(1, len(xs)):
        ans[i-1] = num * (xs[i] - xs[i-1])
        num += 1
    return ans