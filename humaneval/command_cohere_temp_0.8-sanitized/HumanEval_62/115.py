def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed as a list of coefficients.
    
    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power of x.
    
    Returns:
        list: Derivative of the polynomial as a list of coefficients.
    """
    result = [0] * len(xs)
    result[0] = 1
    for i in range(1, len(xs)):
        result[i] = result[i - 1] * 2 + xs[i]
    return result