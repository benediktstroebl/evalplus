
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
    if '.' in x and '/' in x:
        if '/' in n and n[1] != 0:
            numerator, denominator = x.split('/')
            numerator, denominator = ratioToFraction(numerator, denominator)
            numerator = int(numerator)
            denominator = int(denominator)
            numerator *= int(n)
            if numerator % denominator == 0:
                return True
            else:
                return False
        else:
            if float(x) * int(n) == int(x) * float(n):
                return True
            else:
                return False
    else:
        if int(x) * int(n) == int(x) * int(n):
            return True
        else:
            return False

