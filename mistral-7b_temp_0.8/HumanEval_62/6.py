

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    ans = []
    num_coeffs = len(xs)
    for idx in range(num_coeffs):
        # the idxth coefficient is the derivative of xs[idx] + xs[idx+1] * x + ...
        # if xs[idx+1] is 0, then the derivative is xs[idx]
        # if xs[idx+1] is non-zero, then the derivative is xs[idx+1] + xs[idx+2] * x + ...
        # here we calculate derivative of xs[idx] + xs[idx+1] * x + ...
        if idx == 0:
            ans.append(xs[idx])
        else:
            # ans[idx] = xs[idx+1] + xs[idx+2] * x + ...
            ans.append(xs[idx] * (idx + 1))
    return ans

