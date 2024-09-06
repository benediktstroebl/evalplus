import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients * x^i = 0.
    Returns only one solution, even in case of multiple zeros.
    Works only for lists with even number of coefficients,
    and assumes the list contains the coefficient with the largest absolute value.
    """
    # your code here :)

    # check preconditions
    if len(coefficients) % 2 == 1:
        raise ValueError("list of coefficients must have even length")

    # you can assume coefficients contains max_abs_coefficient
    max_abs_coefficient = max(coefficients, key=abs)

    # we construct a matrix with 3 columns:
    # 1) coefficients relative to max_abs_coefficient
    # 2) coefficients scaled with max_abs_coefficient
    # 3) column of zeros
    coefficients_scaled = [coeff / max_abs_coefficient**i for i, coeff in enumerate(coefficients)]
    coefficients_scaled.extend([0] * (len(coefficients) - len(coefficients_scaled)))

    # construct matrix
    A = [[coefficients_scaled[i * 2 + j] for j in range(len(coefficients_scaled) // 2)]
                for i in range(len(coefficients_scaled) // 2)]

    # fetch inverse
    try:
        invA = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        raise ValueError("polynomial does not have a zero")

    # inverse is a 2x2 matrix, so we grab x from there
    return invA[0, 0] + invA[1, 0] * 1.0