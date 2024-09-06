def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.
    Args:
        xs (list): List of coefficients where xs[0] is the constant term
            and xs[1] * x + xs[2] * x^2 + ... is the polynomial.
    Returns:
        list: List of coefficients of the derivative, in the same form.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + i
    return result