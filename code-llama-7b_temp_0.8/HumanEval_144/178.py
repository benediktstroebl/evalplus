
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
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    a, b = x.split("/")
    c, d = n.split("/")

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    # print(a, b, c, d)

    if (b != 1) and (d != 1):
        d_gcd = gcd(b, d)
        if d_gcd > 1:
            d //= d_gcd
            b //= d_gcd

        if (a % b == 0) and (c % d == 0):
            a //= b
            c //= d
            # print(a, b, c, d)

    if (a == 1) and (c == 1):
        return True
    else:
        return False
