import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients yielding poly(x) = 0.
    Returns only one solution, even if there are more.
    Works only for lists with even numbers of coefficients,
    and assumes the largest non-zero coefficient is the last one.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("find_zero works for polynomials with even numbers of coefficients. You have: " + len(coefficients))

    max_coeff = max(coefficients)
    if max_coeff == 0:
        raise ValueError("find_zero assumes the largest non-zero coefficient is the last one. You have all zeros.")

    # we subtract max_coeff to both sides of equation and get
    # (x-1)*...*(x-n) = -max_coeff
    # If we expand that and compare to original polynomial,
    # we get x^n + ... + x^1 + x^0 = -max_coeff
    # where each ... is a copied x factor, and each x^n, ..., x^1 are
    # coefficients from original polynomial in reversed order.
    # So if we divide both sides by x-1 we get x = -max_coeff / (n+1)
    return -max_coeff / (len(coefficients) + 1)