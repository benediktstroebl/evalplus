def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial represented by a list of coefficients.
    
    Args:
        xs (list): List of coefficients where xs[0] is the constant term and xs[1:] are the powers of x.
    
    Returns:
        list: List of derivatives for each term.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + 1
    
    return result