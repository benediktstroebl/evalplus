import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Only returns the first solution, if multiple solutions exist.
    Guarantees a solution if coefficients have an even number of elements 
    and the largest non-zero coefficient is positive.
    """
    # Check if list has an even number of elements and largest coefficient is positive
    if len(coefficients) % 2 == 0 and coefficients[-1] > 0:
        # Calculate x for equation pi * x = -coefficients[0] / coefficients[1]
        root = -coefficients[0] / coefficients[1]
        # Filter out solutions outside of [-1, 1]
        if -1 <= root <= 1:
            return root
        else:
            # If not, repeat for other coefficients until a solution is found
            for i in range(2, len(coefficients)):
                root = -coefficients[0] / coefficients[i]
                if -1 <= root <= 1:
                    return root
    else:
        raise ValueError("List of coefficients must have an even number of elements and a positive leading coefficient.")