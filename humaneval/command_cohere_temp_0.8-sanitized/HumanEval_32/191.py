import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.

    Preconditions:
        - coefficients must be an even-length list with the largest non-zero coefficient first.
    """
    # your code here
    # You can use the following code as a starting point:
    if len(coefficients) % 2 == 0:
        # rearrange coefficients to put largest to first
        coefficients = coefficients[::-1]
        largest_coeff = coefficients[0]
        midsize_coeff = coefficients[1]
        small_coeff = 0
        for i in range(2, len(coefficients)):
            if coefficients[i] != 0:
                small_coeff += coefficients[i] / (i + 1)
        x = -largest_coeff / midsize_coeff
        x += small_coeff / math.pow(midsize_coeff, 2)
        return x
    else: 
        raise ValueError("coefficients list must have an even number of elements and largest coefficient first.")