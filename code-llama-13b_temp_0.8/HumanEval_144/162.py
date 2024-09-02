
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
    x_n = x.split('/')
    x_d = x_n[1]
    x_n = x_n[0]
    n_n = n.split('/')
    n_d = n_n[1]
    n_n = n_n[0]
    x_n = int(x_n)
    x_d = int(x_d)
    n_n = int(n_n)
    n_d = int(n_d)
    if (x_n * n_d) % x_d == 0 and (n_n * x_d) % n_d == 0:
        return True
    return False
