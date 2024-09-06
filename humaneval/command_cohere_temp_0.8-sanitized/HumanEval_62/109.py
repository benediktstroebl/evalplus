def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.

    Args:
        xs (list): Coefficients of the polynomial in the format [xs[0], xs[1] * x, xs[2] * x^2, ...]

    Returns:
        list: Derivative of the polynomial in the same format [xs[0], xs[1] * x, xs[2] * x^2, ...]
    """

    # Initialize an empty list to store the result
    result: list = []

    # Ensure that the input is a list
    if not isinstance(xs, list):
        raise TypeError("Input xs must be a list")

    # Check if the list is empty
    if not xs:
        return result

    # Iterate through the list of coefficients
    for i in range(len(xs)):
        result.append(xs[i] + sum(j * (i + 1) for j in xs[i+1:]))

    return result