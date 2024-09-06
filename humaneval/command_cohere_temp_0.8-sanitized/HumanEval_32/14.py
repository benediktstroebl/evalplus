import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the coefficients.
    Works only for polynomials with an even number of coefficients,
    and assumes the largest non-zero coefficient is the term with the largest power.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("Polynomial must have an even number of coefficients")
    max_pow = len(coefficients) - len(coefficients) // 2 - 1
    max_coeff = coefficients[max_pow]

    if max_coeff == 0:
        raise ValueError("Polynomial must have a non-zero coefficient")

    # Divide the polynomial by the max power term
    reduced_coefficients = [
        coefficient / max_coeff
        for coefficient in coefficients
        if coefficient != 0
    ]
    root_sum = sum(
        [
            coefficient
            * math.pow(-1, i)
            / (i + 1)
            for i, coefficient in enumerate(reduced_coefficients)
        ]
    )

    return root_sum