
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
    # split the input string into numerator and denominator
    x_parts = x.split("/")
    n_parts = n.split("/")

    # check if x and n are valid fractions
    if int(x_parts[1]) == 0:
        return False
    if int(n_parts[1]) == 0:
        return False

    # check if x is a proper fraction (i.e. not equal to 1)
    if int(x_parts[1]) == 1:
        return False

    # if x is a proper fraction, check if n is a proper fraction as well
    if int(n_parts[1]) == 1:
        return False

    # check if x and n have the same denominator
    if int(x_parts[0]) != int(n_parts[0]):
        return False

    # if x and n have the same denominator, simplify the fraction by finding the common numerator
    common_numerator = int(x_parts[0]) * int(n_parts[1])

    # check if the simplified fraction is a whole number
    if int(x_parts[1]) == common_numerator % 1:
        return True

    return False