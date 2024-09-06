
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
    x_list = x.split("/")
    n_list = n.split("/")

    if x_list[0] == "0" or n_list[0] == "0":
        return False

    if (
        x_list[0] == "1"
        and int(x_list[1]) == 1
        and x_list[1] == n_list[1]
        and int(n_list[0]) == 1
    ):
        return True

    return False

