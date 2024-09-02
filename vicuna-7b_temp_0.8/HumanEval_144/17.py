
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
    # split the input string
    n_str, x_str = n.split("/")
    # convert x, and n to float
    n_num = float(n_str)
    x_num = float(x_str)
    # check the denominator of x
    if x_num != 1:
        return False
    # check the numerator of x
    if n_num % x_num != 0:
        return False
    # convert n to float
    n_num = float(n)
    # check if the result is a whole number
    return n_num % 1 == 0
