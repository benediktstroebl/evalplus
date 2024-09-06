
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

    if x == '0' or n == '0':
        return False

    a = x.split('/')
    b = n.split('/')

    if a[0] == '0' or b[0] == '0':
        return False

    a[0] = int(a[0])
    a[1] = int(a[1])
    b[0] = int(b[0])
    b[1] = int(b[1])

    if a[1] == b[1]:
        return True
    else:
        return False
