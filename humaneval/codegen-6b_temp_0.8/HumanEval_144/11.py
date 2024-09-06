
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
    # quick and dirty solution
    x = x.split('/')
    n = n.split('/')
    if int(x[0]) / int(n[0]) == int(x[1]) / int(n[1]):
        return True
    else:
        return False


"""
    --- Part Two ---

    You do not have to worry about if your fractional_simplifier function is
    correct and will pass the tests. You must make sure that it does not change
    the result of any fraction from the example above, and that it correctly
    simplifies all of the fractions in the file.

    For example,

    simplify("4/6", "5/4") is not equal to 1/3.

    simplify("4/6", "13/4") gives 1/3, as expected.

    simplify("5/4", "2/3") is not equal to 1/3.

    simplify("5/4", "4/3") is not equal to 1/3.

    simplify("5/4", "2/3") is not equal to 1/3. This is the fraction you
    obtained from the previous challenge.

    What is the most significant digit that is common to all fractions in the
    file?
"""

