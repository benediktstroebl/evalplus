def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    ans = [0]*(len(xs)-1)
    dx = 1
    for i in range(len(xs)-1):
        ans[i] = xs[i+1] * dx
        dx *= i+2
    return ans