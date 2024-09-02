
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
    x_spl = x.split("/")
    n_spl = n.split("/")

    x_num = int(x_spl[0])
    x_den = int(x_spl[1])

    n_num = int(n_spl[0])
    n_den = int(n_spl[1])

    if x_den * n_den / (x_num * n_num) == int(x_den * n_den / (x_num * n_num)):
        return True
    return False

