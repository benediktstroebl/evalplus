
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

    if (x == "1/0" or n == "0/1") or (x == "0/1" or n == "1/0"):
        return False

    if x[0] == "0" and n[0] == "0":
        return False

    xn = x.split("/")
    nx = n.split("/")

    xn[0] = int(xn[0])
    nx[0] = int(nx[0])

    xn[1] = int(xn[1])
    nx[1] = int(nx[1])

    if xn[0] == 0:
        return False

    if nx[0] == 0:
        return True

    if xn[1] == 0:
        return False

    if nx[1] == 0:
        return True

    if xn[1] == nx[0]:
        return True

    if xn[0] % nx[0] == 0:
        return True

    if nx[0] % xn
