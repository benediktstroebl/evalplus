

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # try to find the pattern here, we can see that the derivative of the polynomial is a polynomial in itself
    # but we dont know the order of the polynomial, it can be up to any order
    # so the order of the new polynomial is the same as the old one
    # now we can see that each of the coefficients in the new polynomial are the same as the coeff of the old polynomial
    # but each coefficient is multiplied by the previous order + 1
    # for example if the polynomial was of order 5, then the coefficient of 0th order is 1 and multiplied by 0+1, giving 1
    # 1st order is 2nd order coeff * 1+1, which is 2
    # 2nd order is 3rd order coeff * 2+1, which is 6
    # 3rd order is 4th order coeff * 3+1, which is 12
    # 4th order is 5th order coeff * 4+1, which is 20
    # 5th order is 6th order coeff * 5+1, which is 30

    # we can take advantage of the 2nd derivative of the polynomial, so the first thing we do is we find the 2nd derivative
    # 2nd derivative is the same as the first derivative but multiplied by the previous order
    # for example if the polynomial was of order 5, then the coefficient of 0th order is 20 and multiplied by 0 * 1, giving 20
    # 1st order is 4th order coeff * 1 * 1, which is 4
    # 2nd order is 6th order coeff * 2 * 1, which is 12
    # 3rd order is 8th order coeff * 3 * 1, which is 36
    # 4th order is 10th order coeff * 4 * 1, which is 80
    # 5th order is 12th order coeff * 5 * 1, which is 140

    # so if we take the original polynomial and multiply it by its derivative, we get the second derivative
