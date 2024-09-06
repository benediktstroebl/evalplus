import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Parameters:
        - coefficients: A list of numbers representing the coefficients of the polynomial.
        - x: The point at which to evaluate the polynomial.

    Returns:
        - The value of the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.

    Parameters:
        - coefficients: A list of numbers representing the coefficients of a polynomial.

    Returns:
        - A float representing a solution x for the equation polynomial = 0.
    Coursemer:
        - There will only be one solution, and it will be returned.
        - This function only accepts lists of coefficients that have an even length 
        - And the list must end with the coefficient with the largest absolute value. 
    """
    # your code here
    # Example usage
    # Ex. find_zero([1, 2]) -> -0.5 
    # Ex. find_zero([-6, 11, -6, 1]) -> 1.0 
    if len(coefficients) % 2 == 1 or max(abs(coefficients)) == 0:
        return "coefficients list must have an even length and end with the coefficient with the largest absolute value"
    x0 = 0
    x1 = 1
    num_iterations = 0
    while True:
        val_at_x0 = poly(coefficients, x0)
        val_at_x1 = poly(coefficients, x1) 
        if val_at_x0 == 0 and val_at_x1 == 0:
            return ("Cannot find unique solution for"
                    " polynomial = 0. Returning one solution: %s" % (x0,))
        if val_at_x0 == 0:
            x1 = x0
        elif val_at_x1 == 0:
            x0 = x1
        else:
            x0 += x1 - x0
            x1 += x0 - x1
        num_iterations += 1
        if num_iterations > 10000:
            return ("Cannot find solution for"
                    " polynomial = 0. Exceeded number of iterations.")