import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists of even numbers of coefficients, and coefficients are assumed sorted by size.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # Handling case where list has even number of coefficients and largest non-zero coefficient.
    # We split the list and find zero for each part.
    while coefficients[0] == coefficients[1]:
        coefficients = coefficients[2:]
    if not coefficients:
        return 0

    x0 = find_zero([coefficients[i] for i in range(len(coefficients)) if i % 2 == 0])
    x1 = find_zero([coefficients[i] for i in range(len(coefficients)) if i % 2 == 1])

    # We step by step reduce the interval where the solution is trapped
    # The solution is trapped in interval [-b, b] where polynomial have equal coefficients
    # corresponding to powers of x0 and x1
    while x0 != x1:
        if coefficients[0] != coefficients[1]:
            x0 = (x0 + x1) / 2
            coefficients = [coeff * math.pow(x0, i) for i, coeff in enumerate(coefficients)]
        else:
            # In some cases the coefficients can be equal even after refinement of x0 and x1
            # so we apply refinement one more time.
            x0 = (x0 + x1) / 2
            x1 = (x0 + x1) / 4
            coefficients = [coeff * math.pow(x0, i) for i, coeff in enumerate(coefficients)]

    return x0