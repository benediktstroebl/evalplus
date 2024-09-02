
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
    x_n = f"{x}/{n}"
    if x_n.split('/')[0] == '0':
        return False
    if x_n.split('/')[1] == '1':
        return True
    if x_n.split('/')[0] == x_n.split('/')[1]:
        return False
    return True

