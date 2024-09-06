import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only the first found zero.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    assert len(coefficients) % 2 == 0, "List should have even number of elements"
    max_coeff = max(coefficients)
    assert max_coeff != 0, "Largest coefficient must be non-zero"

    # Solution based on symmetry
    # smallest zero adds distance to largest coefficient
    # rest of the zeros are at equal distances to closest zero
    # when we traverse coefficients in reverse,
    # we increase distance to closest zero gradually
    zero_dist = max_coeff // 2
    x = zero_dist + 0.01
    for i in range(len(coefficients) - 1, -1, -1):
        x_prev = x
        x = (x_prev - coefficients[i] / zero_dist)
        zero_dist += coefficients[i] / zero_dist

    return x