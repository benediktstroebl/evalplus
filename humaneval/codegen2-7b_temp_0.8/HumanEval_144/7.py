
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
    x_numerator = x.split('/')[0]
    x_denominator = x.split('/')[1]
    n_numerator = n.split('/')[0]
    n_denominator = n.split('/')[1]
    x_num = int(x_numerator)
    n_num = int(n_numerator)
    x_denom = int(x_denominator)
    n_denom = int(n_denominator)
    return (x_num * n_num == x_denom * n_denom) and (x_num!= 0 and n_num!=
