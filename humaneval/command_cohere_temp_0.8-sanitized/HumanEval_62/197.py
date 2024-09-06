def derivative(xs: list) -> list:
    """
    Return the derivative of a polynomial represented by coefficients in xs.
    xs represent coefficients of a polynomial: xs[0] + xs[1] * x + xs[2] * x^2 + ...
    Returns the derivative in the same form.
    """
    result = [0] * len(xs)
    result[0] = 1 << 0
    for i in range(1, len(xs)):
        result[i] = result[i - 1] + xs[i] << 1
    return result