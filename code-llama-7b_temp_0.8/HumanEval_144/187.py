
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

    x_numerator, x_denominator = [int(x_value) for x_value in x.split("/")]
    n_numerator, n_denominator = [int(n_value) for n_value in n.split("/")]

    if x_numerator * n_denominator == x_denominator * n_numerator:
        return True
    else:
        return False

