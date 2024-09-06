
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

    import re
    from fractions import Fraction
    
    p = re.compile(r"^(\d+)(/(\d+))?$")
    fraction_1 = p.findall(x)
    fraction_2 = p.findall(n)

    x = Fraction(int(fraction_1[0][0]), int(fraction_1[0][1]))
    n = Fraction(int(fraction_2[0][0]), int(fraction_2[0][1]))
    if x.numerator == 0 or n.numerator == 0:
        return False
    else:
        return x.denominator == n.denominator
    
    
