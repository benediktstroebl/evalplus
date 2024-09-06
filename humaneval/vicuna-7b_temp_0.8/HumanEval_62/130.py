

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return xs

def sage(f):
    """
    Given a function f(x) in the form of f(x) = a0 + a1*x + a2*x^2 + ....,
    return the sum of the reciprocals of its coefficients.
    >>> sage(f=lambda x: x)
    1/1
    >>> sage(f=lambda x: x**2)
    (1/1)^2 + (1/1) \* 2
    >>> sage(f=lambda x: x**3)
    (1/1)^3 + (1/1)^2 \* 3
    """
    coeffs = list(map(float, f(x).split(x)))
    reciprocals = [1/coeff for coeff in coeffs]
    return sum(reciprocals)

print(sage(derivative([3, 1, 2, 4, 5])))
print(sage(derivative([1, 2, 3])))