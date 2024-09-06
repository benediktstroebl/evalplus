

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # ------------------------------------------------------------------------------------------------------------------
    # your code here
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # result = []
    # for i in range(1, len(xs)):
    #     result.append(xs[i]*i)
    # return result

    # iterative solution
    # xs = [1, 2, 3]
    # result = []
    # for i in range(0, len(xs)-1):
    #     result.append(xs[i]*(i+1))
    # return result

    # recursive solution
    def recursive_derivative(xs: list, i: int) -> list:
        """
        :param xs: input list, for example [1, 2, 3]
        :param i: index of the list
        :return: list containing derivative of xs, e.g. [2, 6]
        """
        if i == 0:
            return []
        if i == 1:
            return
