import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients such that poly(x) = 0.
    Returns only the first found zero solution, even if there are more.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient, as it guarantees a solution.
    """
    def find_solution(coefficients, distinction):
        if len(coefficients) % 2 == 1 or coefficients[0] == 0:
            return None

        x = abs(coefficients[0] / distinction)
        solution = poly(coefficients, x)
        if solution == 0:
            return x

        # Increment solution by precision of calculation
        solution = round(solution, precision)
        if solution > 0:
            return None

        return find_solution(coefficients, distinction / x)

    precision = 10**-10  # Limit of floating point calculation accuracy
    return find_solution(coefficients, max(coefficients) * precision)