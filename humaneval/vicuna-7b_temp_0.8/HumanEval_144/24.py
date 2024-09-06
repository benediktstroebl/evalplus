
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
    # convert x and n to float
    x_float = float(x)
    n_float = float(n)
    # check if x and n have different denominators
    if x_float != n_float:
        return False
    # check if the denominator is not zero
    if n_float != 1:
        return True
    # check if the numerator is greater than the denominator
    if x_float * n_float > 1:
        return True
    # check if the numerator is less than the denominator
    if x_float * n_float < 1:
        return False
    # check if the numerator is equal to the denominator
    if x_float * n_float == 1:
        return True
    # check if the numerator is zero
    if x_float == 0:
        return False
    # check if the denominator is zero
    if n_float == 0:
        return True
    # if none of the above conditions are met, the expression is not a whole number
    return False