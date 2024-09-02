
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

    def get_fraction(s):
        return tuple(int(x) for x in s.split("/"))

    def mul(x, y):
        return x[0] * y[0], x[1] * y[1]

    def eq(x, y):
        return x[0] * y[1] == x[1] * y[0]

    fx = get_fraction(x)
    fn = get_fraction(n)

    return eq(mul(fx, fn), (fx[0] * fn[0], fx[1] * fn[1]))

