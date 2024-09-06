import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    # your code here :)

    # Assurance that we have an even number of coefficients
    if len(coefficients) % 2 == 1:
        print(
            "find_zero function works only with lists of coefficients "
            + "that have even number of items."
        )
        return None

    # sort coefficients descending
    coefficients.sort(reverse=True)

    # Separates even and odd coefficients
    even_coeffs = [coef for coef in coefficients if coef % 2 == 0]
    odd_coeffs = [coef for coef in coefficients if coef % 2 != 0]

    # Assuming largest coefficient is not zero
    x0 = -coefficients[0] / (2 * coefficients[1])
    x1 = (coefficients[0] - 2 * coefficients[1]) / (2 * coefficients[2])

    # Start with affordable precision
    precision = 10 ** -2

    # Lists for storing approximations and results
    approximations = [x0, x1]
    intersections = [None, None]

    while len(odd_coeffs) > 0:
        # Calculate new approximations
        for i in range(len(odd_coeffs)):
            x_prev = approximations[i]
            for sign in [-1, 1]:
                x_next = x_prev + sign * precision * odd_coeffs[i]
                if abs(x_next) < 1e-6:
                    continue
                approximations.append(x_next)

        # Calculate intersections between lines
        for i in range(len(even_coeffs)):
            denominator = (
                even_coeffs[i] * approximations[i] - even_coeffs[i + 1] * approximations[i + 1]
            )
            if denominator == 0:
                continue
            for j in range(len(even_coeffs)):
                if i == j:
                    continue
                numerator1 = even_coeffs[i] * approximations[j] - even_coeffs[j] * approximations[i]
                numerator2 = even_coeffs[i + 1] * approximations[j] - even_coeffs[j + 1] * approximations[i]
                intersections.append(
                    numerator1 / denominator,
                )
                intersections.append(
                    numerator2 / denominator,
                )

        # Filter out unnecessary approximations and intersections
        while len(odd_coeffs) > 0 and len(even_coeffs) > 0 and approximations[0] == approximations[-1]:
            odd_coeffs.pop()
            even_coeffs.pop()
            intersections.pop()
            intersections.pop()

        # Update coefficients for the next loop