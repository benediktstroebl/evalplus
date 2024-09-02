
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
    from math import gcd
    if x == '1' and n == '1':
        return True
    elif x == '1' and n != '1':
        return False
    elif n == '1' and x != '1':
        return False

    x = x.split('/')
    n = n.split('/')
    x = int(x[0])
    n = int(n[0])
    denominator = int(x[1])
    numerator = int(n[1])
    gcd = gcd(numerator,denominator)
    x_new = str(x[0])
    n_new = str(n[0])
    x_new = str(x_new + '/' + str(denominator/gcd))
    n_new = str(n_new + '/' + str(numerator/gcd))
    if x_new == n_new:
        return True
    else:
        return False


