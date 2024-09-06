import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as sum(coeff * x^i for i, coeff in enumerate(coefficients)).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution founds, in case there are multiple zeros.

    Only accepts lists of even numbers of coefficients, and checks that the list contains the largest coefficient.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return "Error: List of coefficients must have an even number of elements and contain the largest coefficient."

    # Make sure that we have an even number of coefficients and that the list contains the largest non-zero coefficient
    # This is important to guarantee that we will find a solution
    x = find_zero_bruteforce(coefficients)
    return x
def find_zero_bruteforce(coefficients: list) -> float:
    """
    Brute force algorithm to find zero of polynomial.
    Simply runs through possible x values and checks if poly(x) = 0.
    This algorithm is far from efficient, but serves as a simple illustration.
    In a real setting you would use e.g. newton method.
    """
    x_values = list(range(0, 10))
    for x in x_values:
        if poly(coefficients, x) == 0:
            return x
    return None