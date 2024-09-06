import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0 to len(coefficients)-1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients, with the largest coefficient non-zero.
    """
    # Make sure list is of even length and largest coeff is non zero
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Coefficients list must have an even length and the largest coefficient cannot be zero."

    # Divide coefficients by the largest coefficient
    coefficients = [val / max(coefficients) for val in coefficients]

    # Sort coefficients backwards
    coefficients.sort(reverse=True)

    # Initialize guess
    x = 1

    # Iterate up to precision
    for _ in range(1000):
        # Evaluate polynomial
        poly_result = poly(coefficients, x)

        # If polynomial is equal to zero
        if poly_result == 0:
            return x

        # Calculate derivative
        poly_prime = [coef * (1 + int(math.log(x)/math.log(2)) ) for coef in coefficients]

        # Calculate new guess
        x_next = x - poly_result / poly(poly_prime, x)

        # Bound iteration
        if x_next <= 0 or x_next >= 2:
            break

        # Update x
        x = x_next

    return "Failed to converge after 1000 iterations."