
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
    def is_whole(x):
        return float(x) - floor(float(x)) < 1e-8

    def gcd(a, b):
        if b == 0:
            return a
        r = a % b
        return gcd(b, r)

    a, b = map(int, x.split('/'))
    g = gcd(a, b)

    return is_whole(a / g) and is_whole(b / g)

