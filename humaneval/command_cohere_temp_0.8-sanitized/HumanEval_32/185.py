import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Args:
        coefficients (list): A list of floats representing the polynomial coefficients in order of increasing power.
        x (float): The point at which the polynomial needs to be evaluated.
    
    Returns:
        float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation poly(x) = 0.
    
    Args:
        coefficients (list): A list of floats representing the polynomial coefficients in order of increasing power.
            The list should have an even number of coefficients and should not be empty.
    
    Returns:
        float: The solution x such that poly(x) = 0. Returns only the single distinct solution.
    """
    if len(coefficients) % 2 == 1 or not coefficients:
        return "Invalid input for polynomial coefficients."
    
    # Ensure coefficients are sorted by power (in case input is not ordered).
    coefficients.sort(key=lambda x: x[0])
    
    # Perform power iteration to approximate the largest real root.
    n = len(coefficients)
    max_iterations = 100000  # Practical limit for the power method.
    x = coefficients[n // 2][1] / coefficients[n // 2][0]
    for _ in range(max_iterations):
        x = x * x / coefficients[n // 2][0]
        if abs(x) < 1e-5:
            break
    
    # Calculate polynomial value at x and negate x to find a zero.
    zero_x = -1 * poly(coefficients, x)
    return zero_x