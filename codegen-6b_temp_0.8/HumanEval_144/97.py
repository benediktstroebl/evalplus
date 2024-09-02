
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
    def fraction_decomposer(x):
        if '/' not in x:
            return x, 1
        else:
            numerator, denominator = x.split('/')
            return int(numerator), int(denominator)

    def fraction_simplifier(numerator, denominator):
        if numerator == 1:
            return True
        elif numerator > denominator:
            return False
        else:
            return True

    def ratio_simplifier(numerator, denominator):
        if numerator == 0 or denominator == 0:
            return True
        elif numerator == denominator:
            return True
        elif numerator > denominator:
            return False
        else:
            return True

    x, n = fraction_decomposer(x)
    fraction_simplified = fraction_simplifier(x, n)

    if fraction_simplified:
        return True
    else:
        return ratio_simplifier(x, n)
