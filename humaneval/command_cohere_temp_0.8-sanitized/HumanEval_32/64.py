import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    
    Preconditions:
    - coeffs is an even-length list of coefficients, with the largest non-zero coefficient at even indices.
    
    Returns: the solution x.
    """
    # your code here
    # You can use the following code as a reference:
    if len(coefficients) % 2 == 1:
        raise ValueError("coefficients list must have an even length.")
    max_index = len(coefficients) // 2
    max_coeff = coefficients[max_index]
    if max_coeff == 0:
        raise ValueError("largest coefficient must be non-zero.")
    x = -max_coeff / (max_index + 1)
    temp_sum = sum([math.pow(x, i) for i in range(max_index, -1, -1)])
    if temp_sum == 0:
        return x
    else:
        return find_zero([coefficients[i] - temp_sum for i in range(max_index, -1, -1)])