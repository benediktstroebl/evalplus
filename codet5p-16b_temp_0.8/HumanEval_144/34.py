
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

    numerator_1, denominator_1 = x.split("/")
    numerator_2, denominator_2 = n.split("/")
    num_1 = int(numerator_1)
    num_2 = int(numerator_2)
    den_1 = int(denominator_1)
    den_2 = int(denominator_2)
    if num_1 * den_2 == num_2 * den_1:
        return True
    else:
        return False
