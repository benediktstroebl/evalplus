from fractions import Fraction
def simplify(x, n):
    x = Fraction(x)
    n = Fraction(n)
    return x * n == Fraction(n.numerator * x.denominator, x.numerator * n.denominator)