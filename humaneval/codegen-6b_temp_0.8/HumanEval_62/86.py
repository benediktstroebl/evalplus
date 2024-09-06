

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    #print(len(xs))
    if len(xs) == 1:
        return [1]
    if len(xs) == 2:
        return [xs[1], xs[0]]
    # ith order derivative is the sum of all jth orders from 0 to i-1
    # i-1th order derivative is just the ith element of this list
    deriv =[]
    for i in range(len(xs)):
        for j in range(i,len(xs)):
            if j == 0:
                deriv.append(xs[i])
            else:
                deriv.append(xs[i]*j)
    return deriv
