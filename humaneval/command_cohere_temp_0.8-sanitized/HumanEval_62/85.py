def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial encoded in a list of coefficients.

        Args:
            xs (list): List of integers, where xs[i] is the coefficient of x^i in the polynomial.

        Returns:
            list: A list of integers, where xs[i] is the coefficient of x^(i+1) of the derivative.
        """

    ans = [0]*len(xs)
    for i in range(len(xs)):
        temp = xs[i]
        for j in range(i):
            temp -= xs[j]*(i-j)
        ans[i] = temp
    return ans