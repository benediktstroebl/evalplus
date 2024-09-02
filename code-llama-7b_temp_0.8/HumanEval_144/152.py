
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
    # you can use python in-built function to find the numerator and denominator
    # use float() to convert string to float.
    x_numerator = float(x.split("/")[0])
    x_denominator = float(x.split("/")[1])
    n_numerator = float(n.split("/")[0])
    n_denominator = float(n.split("/")[1])

    # to find the fraction, the numerator is multiplied by the denominator of n, then divided by the denominator of x
    fraction = (x_numerator * n_denominator) / x_denominator

    # if the fraction evaluates to a whole number, it is a simplified fraction
    if fraction.is_integer():
        return True
    return False
