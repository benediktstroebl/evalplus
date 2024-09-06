import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only the first found zero.
    Works only for lists with even number of coefficients,
    and assumes the list contains the coefficients of the polynomial in increasing order.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements.")
    if coefficients[0] == 0:
        raise ValueError("Please provide the largest non-zero coefficient.")

    # Conversion to polynomial equation ax^n + bx^(n-1) + ... + cx + d
    power = len(coefficients) // 2
    a = coefficients[len(coefficients) // 2 - 1]
    b = coefficients[len(coefficients) // 2]

    # Transform the problem to quadratic equation solving
    # https://en.wikipedia.org/wiki/Quadratic_equation
    if power > 2:
        return find_zero(coefficients[:power])
    elif power == 2:
        return find_zero_quadratic(a, b)
    else:
        raise ValueError("polynomial must have at least 2 coefficients")
def find_zero_quadratic(a: float, b: float) -> float:
    """
    Only works for quadratic polynomials (power = 2)
    Finds zero of quadratic equation ax^2 + bx + c = 0
    """
    # Divide quadratic equation mechanically
    denom = b**2 - 4*a*c
    var = (b - a*math.sqrt(denom)) / (2*a)
    if denom < 0:
        return var
    else:
        return var + (b + a*math.sqrt(denom))/(2*a)