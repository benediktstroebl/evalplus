
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
    # parse the x and n into numerator and denominator
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    # multiply x by n
    x_numerator_by_n = int(x_numerator) * int(n_numerator)
    x_denominator_by_n = int(x_denominator) * int(n_denominator)

    # check if the result is an integer
    if x_numerator_by_n % x_denominator_by_n == 0:
        return True
    else:
        return False

    # use the fractions module
    # import fractions
    # fraction_x = fractions.Fraction(x)
    # fraction_n = fractions.Fraction(n)
    # if (fraction_x * fraction_n).denominator == 1:
    #     return True
    # else:
    #     return False

