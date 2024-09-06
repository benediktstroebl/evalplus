
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

    def floatToFraction(n):
        whole_part = int(n)
        fraction_part = n - whole_part
        numerator = whole_part
        denominator = 1
        for i in range(1, whole_part):
            numerator *= i
            denominator *= i
        for i in range(1, int(fraction_part*10)):
            numerator *= i
            denominator *= i
        return numerator, denominator

    if x == "1/1":
        return True
    if n == "1/1":
        return True
    num1, denom1 = floatToFraction(x)
    num2, denom2 = floatToFraction(n)
    if num1%denom1 == 0 and num2%denom2 == 0:
        if num1/denom1 == num2/denom2:
            return True
        else:
            return False
    return False
