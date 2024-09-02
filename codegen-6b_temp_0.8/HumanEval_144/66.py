
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
    if n[0] == '0' or n[1] == '0':
        return False

    numerator = int(n[0:len(n) - len(n.lstrip('0'))])
    denominator = int(n[len(n) - len(n.lstrip('0')):len(n)])

    gcd = get_GCD(numerator, denominator)

    numerator = numerator // gcd
    denominator = denominator // gcd

    if numerator != denominator:
        return False

    return not simplify(str(numerator), str(denominator))
