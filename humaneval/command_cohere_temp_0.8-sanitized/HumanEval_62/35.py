def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    derivative_xs = [0] * n
    for i in range(n):
        xs_i_product = 1
        for j in range(n):
            if j != i:
                xs_i_product *= xs[j]
        derivative_xs[i] = xs[i+1] * xs_i_product
    return derivative_xs