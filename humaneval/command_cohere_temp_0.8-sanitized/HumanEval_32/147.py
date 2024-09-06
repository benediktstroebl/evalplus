import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n = 0.
    Returns only one solution, even if there are many.
    Works only with lists coefficients with even number of coefficients
    and largest non zero coefficient, as it guarantees
    a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "coefficients list should have an even number of items and a non-zero leading coefficient."
    
    # Calculate the leading coefficient
    leading_coefficient = coefficients[0]

    # Divide the polynomial to leading coefficient and the rest
    rest_coefficients = [coeff / leading_coefficient for coeff in coefficients[1:]]

    # Find the solution for the rest polynomial
    x_rest = poly(rest_coefficients, 0)

    # Calculate the solution
    solution = -leading_coefficient / (x_rest)

    # Verify if the solution is correct
    poly_at_solution = poly(coefficients, solution)
    if abs(poly_at_solution) < 1e-5:
        return solution
    else:
        return "The computed solution does not satisfy the polynomial equation."