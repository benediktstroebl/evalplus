
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
    def fraction_to_int(fraction):
        """Returns the integer value of the fraction"""
        return int(fraction.split("/")[0])
    def gcd(a, b):
        """Calculates the greatest common divisor of a and b"""
        if b == 0:
            return a
        return gcd(b, a % b)
    numerator = fraction_to_int(x)
    denominator = fraction_to_int(n)
    gcd_value = gcd(numerator, denominator)
    numerator = numerator // gcd_value
    denominator = denominator // gcd_value
    simplified_fraction = str(numerator) + "/" + str(denominator)
    if float(simplified_fraction) % 1 == 0:
        return True
    else:
        return False



