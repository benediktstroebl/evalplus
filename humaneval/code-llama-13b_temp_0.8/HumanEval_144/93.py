
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
    x_num = x.split("/")[0]
    x_denom = x.split("/")[1]
    n_num = n.split("/")[0]
    n_denom = n.split("/")[1]

    x_num = int(x_num)
    x_denom = int(x_denom)
    n_num = int(n_num)
    n_denom = int(n_denom)
    result = (x_num / x_denom) * (n_num / n_denom)
    if int(result) == result:
        return True
    else:
        return False

