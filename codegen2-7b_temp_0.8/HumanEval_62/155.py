

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    
    if len(xs) <= 1:
        return []
    
    ys = [xs[-1]] # the last element of xs represents the derivative of this polynomial
    
    for i in range(len(xs) - 2, 0, -1):
        ys.append(xs[i] + xs[i + 1] * ys[-1])
        
    return ys
    
