
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

    def gcd(x, y):
        """Greatest common divisor"""
        return x if y == 0 else gcd(y, x % y)

    num1, num2 = x.split("/")
    num1, num2 = int(num1), int(num2)
    den1, den2 = n.split("/")
    den1, den2 = int(den1), int(den2)

    # simplify
    num1 *= den2
    num2 *= den1
    gcd = gcd(num1, num2)

    if num1 / gcd == int(num1 / gcd) and num2 / gcd == int(num2 / gcd):
        return True
    return False




