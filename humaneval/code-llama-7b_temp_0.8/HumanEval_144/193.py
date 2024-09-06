
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

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    n1, d1 = map(int, x.split('/'))
    n2, d2 = map(int, n.split('/'))
    return gcd(n1 * d2, n2 * d1) == 1

    # Alternative solutions:
    # https://stackoverflow.com/a/39226532
    # https://stackoverflow.com/a/53165024
