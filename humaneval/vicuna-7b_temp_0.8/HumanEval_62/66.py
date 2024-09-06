

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if not xs:
        return [1, 0, 0, 0]
    
    if len(xs) == 1:
        return [xs[0], 0, 0, 0]
    
    first_term = xs.pop(0)
    xs_derivative = [0, 0, 0, 0]
    for i in range(len(xs)):
        xs_derivative[i] = xs[i]
        xs_derivative[i+1] = xs[i+1] + xs_derivative[i] * x
        
    return first_term + xs_derivative[-1]
