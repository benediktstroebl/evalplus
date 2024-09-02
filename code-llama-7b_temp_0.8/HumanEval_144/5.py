
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
    num1, denom1 = x.split("/")
    num2, denom2 = n.split("/")

    num1 = int(num1)
    denom1 = int(denom1)
    num2 = int(num2)
    denom2 = int(denom2)

    result = num1 * denom2 / denom1
    return result.is_integer()

