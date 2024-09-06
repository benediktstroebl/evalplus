import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation p(x) = 0.
    Returns the value of x that makes the polynomial equal to zero,
    based on the coefficients provided.
    This function only returns one solution, and works only with lists
    of even numbers of coefficients, and with the coefficient list
    containing at least one non-zero value.
    """
    if len(coefficients) % 2 == 1 or not coefficients:
        return None

    # arrange coefficients in decreasing order
    coefficients.sort(key=lambda x: x/x if x != 0 else float('inf'), reverse=True)

    # extract non zero coefficient
    coeff = coefficients[0]

    # check if there is only one non zero coefficient
    if len(coefficients) == 2:
        # if there is, return it's half
        return coeff / 2

    # handle even number of coefficients