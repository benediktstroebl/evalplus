def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.
    
    Args:
        xs (list): Coefficients of the polynomial, in the order: xs[0] + xs[1] * x + xs[2] * x^2 + ...
    
    Returns:
        list: Derivative of the polynomial in the same form.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 << i
    return result