
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
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def lcm(a, b):
        return int(a * b / gcd(a, b))

    a = Fraction(x)
    b = Fraction(n)

    l = lcm(a.denominator, b.denominator)
    return a.numerator * b.denominator / l == a.denominator * b.numerator / l
