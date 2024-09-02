
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
    a, b = map(int, x.split('/'))
    c, d = map(int, n.split('/'))

    def g(x, y):
        if x / y == 0:
            return 0
        elif x % y == 0:
            return x / y
        else:
            return None

    return a % c == b % d == 0 or g(a, c) is not None and g(b, d) is not None


from fractions import Fraction

