
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

    x_n = x + "/" + n
    if x == "0":
        return True
    elif x == "1/1":
        return True
    else:
        x_split = x.split("/")
        n_split = n.split("/")
        if x_split[0] == n_split[0]:
            return simplify(x_split[1], n_split[1])
        elif x_split[1] == n_split[1]:
            return simplify(x_split[0], n_split[0])
        else:
            return False

