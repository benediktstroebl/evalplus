def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in list form.
    
    Args:
        xs (list): Coefficients of the polynomial, where xs[0] is the constant term and xs[1:] are the terms with multiplied by the variable x^1, x^2, ... etc. 
    
    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
    """
    result = [0] * (len(xs) - 1)
    for i in range(1, len(xs)):
        result[i - 1] = xs[i] * i
    return result