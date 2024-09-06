
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

    if x == '0/1': return False
    if x == '1/1': return True
    x_n = x.split('/')
    n_n = n.split('/')
    x_n[0] = int(x_n[0])
    n_n[0] = int(n_n[0])
    x_n[1] = int(x_n[1])
    n_n[1] = int(n_n[1])
    if x_n[1] % n_n[1] == 0:
        return True
    else:
        return False

