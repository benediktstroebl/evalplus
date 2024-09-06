import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Works only for lists with even number of coefficients,
    and with largest coefficient non-zero
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Coefficients list should have an even length and the largest coefficient cannot be zero."

    # invert coefficients and evaluate at x = 1 to get residues
    residues = [coeff for coeff in coefficients if coeff != 0]
    inverted_poly = [math.pow(x, len(residues)) for x in residues]
    result = sum(inverted_poly) / coefficients[0]

    for i in range(2, 1000):
        x = result + i
        if poly(coefficients, x) == 0:
            return result