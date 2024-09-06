def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by lists of coefficients.
    
    Args:
    - xs (list): Lists of coefficients for a polynomial in decreasing powers of x.
    
    Returns:
    - list: Lists of coefficients for the derivative of the polynomial in decreasing powers of x.
    """
    result = [0]*len(xs)
    result[0] = 1
    for i in range(len(xs)-1):
        result[i+1] = result[i] * len(xs) - xs[i+1]*(len(xs)-1)
    return result