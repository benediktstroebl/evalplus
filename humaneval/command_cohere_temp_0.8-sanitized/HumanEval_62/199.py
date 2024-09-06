def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed as a list of coefficients.
    
    Args:
        xs (list): Coefficients of the polynomial, in order of increasing powers.
    
    Returns:
        list: Derivative of the polynomial as a list of coefficients.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1000000000
    return result