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
        raise ValueError('List of coefficients must not be empty')

    max_coeff = max(coefficients, key=coefficients.count)
    if not max_coeff:
        raise ValueError('List of coefficients must not be empty')

    x = max_coeff / (2 * max_coeff[0])
    approximation = poly(coefficients, x)
    root_found, x = False, x

    while not root_found:
        if approximation < 0.1 and approximation > -0.1:
            root_found = True
        else:
            x -= approximation / max_coeff[0]
            approximation = poly(coefficients, x)

    return x