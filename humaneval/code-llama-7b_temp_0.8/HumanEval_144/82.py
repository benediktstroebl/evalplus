
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

    if '/' not in x or '/' not in n:
        return False

    n_x = int(x.split('/')[0])
    d_x = int(x.split('/')[1])
    n_n = int(n.split('/')[0])
    d_n = int(n.split('/')[1])

    return (n_x * d_n) % d_x == 0 or (d_x * n_n) % d_n == 0
