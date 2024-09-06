import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists of even numbers of coefficients, and skips zero coefficients.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('List of coefficients must have an even number of elements')
    elif not coefficients:
        return None

    max_coeff = max(coefficients)
    if max_coeff == 0:
        return None

    # Create a list of points x with an interval length of max_coeff
    points = [i * max_coeff / 2 for i in range(int(max_coeff * 2))]

    # Evaluate polynomial at each point
    evaluations = [poly(coefficients, x) for x in points]

    # Find index of first zero evaluation
    zero_index = evaluations.index(0)

    return points[zero_index]