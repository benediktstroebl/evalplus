
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

    if x == '0':
        return False
    if n == '0':
        return False
    if n == '1':
        return True
    if int(x) == int(n):
        return True
    if x[0] == '-':
        x = x[1:]
    else:
        x = '+' + x
    if n[0] == '-':
        n = n[1:]
    else:
        n = '+' + n
    if x.split('/')[0] == '0' and n.split('/')[0] == '0':
        return False
    if x.split('/')[0] == '0':
        return True
    if n.split('/')[0] == '0':
        return True
    if x.split('/')[1] == '0' and n.split('/')[1] == '0':
        return False
    if x.split('/')[1] == '0':
        return True
    if n.split('/')[1] ==
