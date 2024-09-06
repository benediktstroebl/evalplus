import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only one solution, even if there are multiple zeros.
    Works only for lists with an even number of coefficients,
    and assumes the list is sorted with the largest coefficient first.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of values.")
    
    if coefficients[0] == 0:
        raise ValueError("Largest coefficient in list must be non-zero.")

    # Check if there are multiple roots
    if coefficients[0] == coefficients[1]:
        return 0.0

    # Handle special cases of lower degree
    if len(coefficients) == 2:
        return -coefficients[1] / (2 * coefficients[0])
    elif len(coefficients) == 4:
        b = 3 * coefficients[0] * coefficients[3] - coefficients[1] * coefficients[2]
        return (-b - math.sqrt(b ** 2 - 12 * coefficients[0] * coefficients[1])) / (6 * coefficients[0])
    else:
        n = len(coefficients)
        b = [0] * (n - 2)
        c = [0] * (n - 1)
        for i in range(n - 2, -1, -1):
            b[i] = 4 * coefficients[i + 2] * b[i + 1] - coefficients[i + 3] * c[i + 1]
            c[i] = coefficients[i + 3] ** 2 - 4 * coefficients[i + 1] * coefficients[i + 2]
        x1 = (-b[-1] - math.sqrt(b[-1] ** 2 - 4 * c[-1])) / (2 * c[-1])
        x2 = (-b[-1] + math.sqrt(b[-1] ** 2 - 4 * c[-1])) / (2 * c[-1])
        return sorted([x1, x2])[0]