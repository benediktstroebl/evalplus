
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
    from math import gcd

    x_n, x_d = x.split("/")
    n_n, n_d = n.split("/")

    assert gcd(int(x_n), int(x_d)) == 1
    assert gcd(int(n_n), int(n_d)) == 1

    # x_n is the numerator of the product of x and n.
    # x_d is the denominator of the product of x and n.
    # x = x_n / x_d
    # n = n_n / n_d
    # x * n = (x_n / x_d) * (n_n / n_d)
    #       = x_n * n_n / (x_d * n_d)
    # So the numerator of x * n is x_n * n_n, and the denominator is x_d * n_d.

    return (int(x_n) * int(n_n) * int(n_d) == int(x_d) * int(n_d))
