
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
    # if x * n simplifies to an integer, return True
    # if not, return False
    # if either x or n is a fraction, return False
    # if x is a decimal, return False
    # if x is an integer and n is a fraction, return False
    # if n is an integer and x is a fraction, return False

    # 10/2 * 2/10 = 10/10 = 1
    # 10/2 * 2/9 = 20/18 = 10/9
    # 10/2 * 2/10 = 2/2
    # 10/2 * 2/11 = 2/22

    # 10/2 * 4/10 = 4/5
    # 10/2 * 4/9 = 8/18 = 4/9
    # 10/2 * 4/11 = 8/22 = 4/11

    # 2 * 3/4 = 6/4 =
