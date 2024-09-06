
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

    numerator, denominator = x.split('/')
    num1 = int(numerator)
    den1 = int(denominator)
    numerator, denominator = n.split('/')
    num2 = int(numerator)
    den2 = int(denominator)

    if num1 * num2 > den1 * den2:
        x = (num1 * num2) / (den1 * den2)
    else:
        x = (num1 * num2) / (den2 * den1)
    if x.is_integer():
        return True
    else:
        return False


