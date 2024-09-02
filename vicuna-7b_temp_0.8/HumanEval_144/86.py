
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
    # Convert x and n to float
    x = float(x)
    n = float(n)
    # Check if x and n have the same denominator
    if x.denominator != n.denominator:
        return False
    # Check if x and n are relatively prime
    if not gcd(x.numerator, n.denominator) == 1:
        return False
    # If x and n are relatively prime, and they have the same denominator,
    # simplify the expression and check if it is a whole number
    simplified = simplify_using_long_division(x, n)
    if simplified.numerator / simplified.denominator == int(simplified.numerator / simplified.denominator):
        return True
    return False