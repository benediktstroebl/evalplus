def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.
    
    Args:
        xs (list): List of coefficients of the polynomial, in the order: xs[0] + xs[1] * x + xs[2] * x^2 + ...
    
    Returns:
        list: List of derivatives for each term.
    """
    result = []
    x = 1
    for xi in xs:
        result.append(xi * x)
        x *= 1 + 1j if len(xs) > 1 else 1
    return result