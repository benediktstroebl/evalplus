import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of terms where each term is a product of coefficient and x raised to the power of its index in coefficients.
    i.e. coefficient[0] * x^0 + coefficient[1] * x^1 + ... + coefficient[n] * x^n

    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The result of evaluating the polynomial at the given point.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation coefficients[i] * x^(i) = 0.
    Will only return one solution, even if there are multiple zeros.

    Args:
        coefficients (list): A list of floats representing the coefficients of a polynomial with even number of coefficients.

    Returns:
        float: A solution x for the polynomial equation.
    """
    # Check if list has an even number of coefficients
    if len(coefficients) % 2 == 1:
        print("Error! List of coefficients must have an even number of elements.")
        return None

    # Sort list of coefficients from largest to smallest
    coefficients.sort(key=lambda x: abs(x), reverse=True)

    # Find the largest non-zero coefficient
    largest_coeff = coefficients[0]

    # Calculate the root using the polynomial division algorithm
    for i in range(1, len(coefficients)):
        temp = coefficients[i]
        for j in range(i, len(coefficients)):
            coefficients[j] = coefficients[j] - temp * poly(coefficients[i:], coefficients[j]) / poly(coefficients[i:j+1], coefficients[i])

    # Return the root
    return coefficients[0]