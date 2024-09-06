def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in sums of powers of x.

        Args:
            xs (list): Coefficients of the polynomial, with xs[0] being the constant term
                and xs[1:] being the terms with powers of x. 

        Example:
            >>> derivative([3, 1, 2, 4, 5])
            [1, 4, 12, 20]
            >>> derivative([1, 2, 3])
            [2, 6]
    """
    result = [0] * (len(xs) - 1)
    result.append(1)
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (i + 1)
    return result