

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # YOUR CODE HERE
    def create_polynomial_object(coefficients):
        def p(x):
            result = 0
            for i in range(len(coefficients)):
                result += coefficients[i] * x**i
            return result
        return p

    def create_polynomial_derivative_object(coefficients):
        def d(x):
            result = 0
            for i in range(1, len(coefficients)):
                result += coefficients[i] * i * x**(i-1)
            result += coefficients[0]
            return result
        return d

    result_list = [x / i for i, x in enumerate(xs)]
    return result_list
