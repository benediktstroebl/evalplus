

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # check if input is a list
    if not isinstance(xs, list) or len(xs) == 0:
        raise TypeError("Input should be a list of integers or a list of integers and coefficients")
    
    # check if input is a polynomial
    if not all(isinstance(c, int) for c in xs):
        raise TypeError("Input should be a list of coefficients")
    
    # handle negative input
    if any(-c for c in xs):
        xs = [-c for c in xs]
    else:
        xs = [0] * (max(len(xs), 1) + 1)
    
    # handle degree 0 polynomial
    if len(xs) == 1:
        return [0]
    
    result = [0] * len(xs)
    for i in range(len(xs)):
        for j in range(i+1, len(xs)):
            result[i] += xs[i] * xs[j]
    
    return result
