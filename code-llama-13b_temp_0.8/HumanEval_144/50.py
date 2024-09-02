
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

    def split(frac):
        return int(frac.split("/")[0]), int(frac.split("/")[1])

    def multiply(frac1, frac2):
        num1, den1 = split(frac1)
        num2, den2 = split(frac2)
        return str(num1 * num2) + "/" + str(den1 * den2)

    return eval(multiply(x, n)) % 1 == 0

