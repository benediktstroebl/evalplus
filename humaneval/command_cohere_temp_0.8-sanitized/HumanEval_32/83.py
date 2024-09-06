import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution for the equation poly(x) = 0.
    Returns the value of x at which the polynomial evaluates to zero.

    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
    Returns:
        float: A float representing the value of x at which the polynomial evaluates to zero.
    """
    # Make sure that the list has even number of elements and the highest non zero element is the last.
    assert len(coefficients) % 2 == 0 and coefficients[-1] != 0, "List of coefficients should have even number of elements and the largest non-zero element at the last position."    
    # Let y be the wanted result. We have:
    # y*y == -coefficients[0] && y == 0
    # So y == 0 or y == sqrt(-coefficients[0])
    return 0 if coefficients[0] == 0 else math.sqrt(-coefficients[0])