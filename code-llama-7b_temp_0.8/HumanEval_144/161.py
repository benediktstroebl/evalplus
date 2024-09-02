
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
    a,b = x.split("/")
    a = int(a)
    b = int(b)
    c,d = n.split("/")
    c = int(c)
    d = int(d)
    gcd = 1
    if(a == 0 or b == 0 or c == 0 or d == 0):
        return False
    else:
        if a == c or b == d:
            return True
        if a%b == 0 and c%d == 0:
            return True
        gcd = find_gcd(a, b, c, d)
        if(gcd != 1):
            return True
        return False
