
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # parse the x string into numerator and denominator
    x_num, x_den = x.split('/')

    # parse the n string into numerator and denominator
    n_num, n_den = n.split('/')

    # compute the numerator and denominator of x * n
    xn_num = int(x_num) * int(n_num)
    xn_den = int(x_den) * int(n_den)

    # compute the GCD of xn_num and xn_den
    gcd = gcd_of_two_numbers(xn_num, xn_den)

    # return if xn_num / gcd is a whole number
    return xn_num // gcd == xn_den // gcd

