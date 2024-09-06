def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs where xs[i] is the coefficient of x^i.

        Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    ans = [0] * (len(xs) - 1)
    for i in range(len(xs)):
        temp = 0
        for j in range(i+1, len(xs)):
            temp += xs[j] * j
        ans[i] = temp
    return ans