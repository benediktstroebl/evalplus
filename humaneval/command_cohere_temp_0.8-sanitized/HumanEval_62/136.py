def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs)):
        result[i] = xs[i+1] * (x + 1) - xs[i]   # diffrence quotiient
        x += 1
    return result