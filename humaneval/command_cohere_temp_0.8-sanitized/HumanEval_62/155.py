def derivative(xs: list) -> list:
    """
    Return the derivative of the polynomial defined by the list of coefficients.
    """
    result = [0] * (len(xs) + 1)
    result[0] = 1
    for i in range(len(xs)):
        for j in range(i+1, len(xs)+1):
            result[j] += xs[i] * (j - i)
    return result