def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by lists of coefficients.
    
    Polynomial is represented as: xs[0] + xs[1] * x + xs[2] * x^2 + ...
    
    Returns derivative in the same form.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        x -= xs[i]
    return result