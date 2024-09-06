import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the given coefficients.
    Returns only the first found zero point, even if there are multiple.
    Requires that the list of coefficients has an even number of items, and the largest non-zero coefficient.
    """
    # Ensure that the list of coefficients has an even number of values and at least 2 items
    if len(coefficients) not in [2, 4, 6, 8] or len(coefficients) == 0:
        raise ValueError("find_zero requires list xs to have an even number of elements and at least 2 elements")

    # Find the largest non-zero coefficient
    max_coeff = max(coefficients, key=coefficients.count)

    # Divide the polynomial to get a quadratic equation
    polynomial_div = [coeff / max_coeff ** 2 for coeff in coefficients if coeff != 0]
    quadratic = polynomial_div + [polynomial_div[-1] / 2]

    # Use the quadratic formula to find the roots of the equation
    discriminant = quadratic[-2] ** 2 - (quadratic[-1] ** 2)
    if discriminant < 0:
        return None  # No real roots, so there is no solution

    # Calculate the two possible solutions for x
    solution1 = math.sqrt(max_coeff ** 2 ** 2 - discriminant) / math.sqrt(2)
    solution2 = -math.sqrt(max_coeff ** 2 ** 2 - discriminant) / math.sqrt(2)

    # Filter the solutions to find the one that satisfies the original polynomial equation
    root_1 = poly(quadratic, solution1)
    root_2 = poly(quadratic, solution2)
    if root_1 == 0 and root_2 == 0:
        return solution1
    elif root_1 == 0 and root_2 != 0:
        return solution2
    elif root_1 != 0 and root_2 == 0:
        return solution1
    else:
        raise ValueError("Failed to find a valid root")