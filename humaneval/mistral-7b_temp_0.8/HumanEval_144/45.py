
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

    import math

    x_list = x.split('/')
    n_list = n.split('/')
    x_num = int(x_list[0])
    x_den = int(x_list[1])
    n_num = int(n_list[0])
    n_den = int(n_list[1])

    if x_den * n_num == x_num * n_den:
        return True
    else:
        return False
