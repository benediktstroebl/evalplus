
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
    n_x = float(x.split('/')[0])
    d_x = float(x.split('/')[1])
    n_n = float(n.split('/')[0])
    d_n = float(n.split('/')[1])

    if ((n_x * d_n) % 1 == 0) and ((n_n * d_x) % 1 == 0):
        return (int(n_x * d_n) == int(n_n * d_x))
    else:
        return False
