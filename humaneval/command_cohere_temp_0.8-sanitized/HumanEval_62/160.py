def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs where xs[0] is the constant term and xs[1:] are the coefficients of the polynomial multiplied by x^{n-1}, n being the index of the term in xs. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * len(xs) - xs[i]
    return result