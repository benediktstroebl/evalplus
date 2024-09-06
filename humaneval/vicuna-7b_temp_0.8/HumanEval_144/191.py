
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
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    # check if x and n are not equal
    if x_denominator != n_denominator:
        return False

    # check if both x and n have a positive numerator
    if not x_numerator or not n_numerator:
        return False

    # check if both x and n have a positive denominator
    if not x_denominator or not n_denominator:
        return False

    # check if both x and n have a positive numerator and denominator
    if x_numerator/x_denominator != n_numerator/n_denominator:
        return False

    # check if x is a factor of n
    if n_numerator % x_numerator == 0:
        return False

    # check if n is a factor of x
    if x_denominator % n_numerator == 0:
        return False

    # check if x and n have a common factor
    if has_common_factor(x_numerator, x_denominator, n_numerator, n_denominator):
        return False

    # simplify x and n if possible
    x_simplified = simplify_numerator(x_numerator)
    n_simplified = simplify_numerator(n_numerator)
    x_simplified = simplify_denominator(x_simplified)
    n_simplified = simplify_denominator(n_simplified)

    simplified_x = x_simplified * n_simplified
    if simplified_x.is_integer() and simplified_x.p % 1 == 0:
        return True
    else:
        return False
