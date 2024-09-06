import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the coefficients.
    Requires an even number of coefficients and assumes the largest non-zero coefficient is the dominant term.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return None

    # Arrange coefficients in descending order and flip to get ascending exponents
    exponents = [i for i in range(len(coefficients))][::-1]
    x = 1
    current_sum = coefficients[exponents.index(len(coefficients) // 2)]

    # Calculate the value of x using the binomial expansion
    for i in range(len(coefficients) // 2):
        term = coefficients[exponents[i]] / (i + 1)
        current_sum -= term
        x *= i + 1
        x //= math.factorial(i)

    return x