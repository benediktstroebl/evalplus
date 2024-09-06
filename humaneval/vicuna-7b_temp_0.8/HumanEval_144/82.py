
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
    # split x and n by '/'
    x_num, x_denom = x.split('/')
    n_num, n_denom = n.split('/')

    # check if x and n have the same denominator
    if x_denom != n_denom:
        return False

    # convert x and n to integers
    x_num = int(x_num)
    n_num = int(n_num)

    # check if x is equal to n
    if x_num == n_num:
        return True

    # check if x and n have the same numerator
    if x_num != 0 and n_num != 0 and x_num/n_num == int(x_num/n_num):
        return True

    # convert the fraction to mixed numeral
    # and check if the mixed numeral is a whole number
    if x_denom == 1:
        x = int(x_num)
        n = int(n_num)
        return x == n
    else:
        return False
