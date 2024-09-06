
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
    a, b = x.split("/")
    c, d = n.split("/")

    # LCM(a, b) = (a * b) / GCD(a, b)
    lcm = (a * b) / gcd(int(a), int(b))
    lcm = str(lcm)

    # GCD(c, d) = GCD(d, c)
    gcd = gcd(int(c), int(d))

    if int(lcm) % int(gcd) == 0:
        return True
    return False

