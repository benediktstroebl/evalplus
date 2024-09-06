
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

    if x == "0/1":
        return True
    elif n == "1/1":
        return False
    elif x.count("/") == 0:
        if n.count("/") == 0:
            return int(x) == int(n)
        else:
            return True
    else:
        num = x.split("/")
        denom = n.split("/")
        if num[0] == denom[0] or denom[0] == "0":
            return simplify(num[1], denom[1])
        else:
            return simplify(num[0] * denom[1] + num[1] * denom[0], denom[1] * denom[0])
