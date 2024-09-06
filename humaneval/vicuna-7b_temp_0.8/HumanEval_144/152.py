
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
    # split x and n
    x_num, x_denom = x.split("/")
    n_num, n_denom = n.split("/")

    # convert to int
    x_num = int(x_num)
    x_denom = int(x_denom)
    n_num = int(n_num)
    n_denom = int(n_denom)

    # check if both are integers
    if x_num == n_num and x_denom == n_denom:
        return True

    # check if x is a whole number
    if x_num == x_denom:
        return True

    # check if n is a whole number
    if n_num == n_denom:
        return True

    # check if x is a whole number and n is not a whole number
    if x_num == x_denom and n_num != n_denom:
        return True

    # check if n is a whole number and x is not a whole number
    if n_num == n_denom and x_num != x_denom:
        return True

    # check if x is not a whole number and n is a whole number
    if not (x_num == x_denom and n_num == n_denom):
        return True

    # check if n is not a whole number and x is a whole number
    if not (x_num == x_denom and n_num == n_denom):
        return True

    return False