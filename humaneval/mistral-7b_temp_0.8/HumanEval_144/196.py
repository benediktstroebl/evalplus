
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

    # x = 1/5, n = 5/1
    # n * x = 1/5 * 5/1
    #       = 1/1
    #  True

    # x = 1/6, n = 2/1
    # n * x = 1/6 * 2/1
    #       = 1/3
    #  False

    # x = 7/10, n = 10/2
    # n * x = 7/10 * 10/2
    #       = 7/2
    #  False

    def gcd(a,b):
        """Function returns the GCD of 2 numbers"""

        while b != 0:
            a,b = b, a%b

        return a

    x, n = [int(i) for i in x.split("/")] , [int(i) for i in n.split("/")]
    return x * n == gcd(x, n)


    # # int("1/5"), int("5
