
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
    # convert x and n to int and denominator
    x_int = int(x)
    n_int = int(n)
    denominator = n_int / x_int

    # check if x and n are valid fractions
    if x_int == 0 or n_int == 0:
        return False
    if denominator == 0:
        return False

    # check if x and n have a common denominator
    if not common_denominator(x_int, denominator) or not common_denominator(n_int, denominator):
        return False

    # check if both x and n are integers
    if x_int == 0:
        return True

    # check if both x and n are irrational numbers
    if abs(x_int) > 1 or abs(n_int) > 1:
        return True

    # check if x and n are equal
    if x_int == n_int:
        return True

    # check if x and n are not equal and are close to each other
    if abs(x_int - n_int) <= 0.01:
        return True

    return False