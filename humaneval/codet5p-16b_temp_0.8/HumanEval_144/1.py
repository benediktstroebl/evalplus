
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

    simplified_x = re.match(r'(.*)\/(.*)', x)
    simplified_n = re.match(r'(.*)\/(.*)', n)

    if simplified_x is None or simplified_n is None:
        return False

    numerator_x = int(simplified_x.group(1))
    denominator_x = int(simplified_x.group(2))

    numerator_n = int(simplified_n.group(1))
    denominator_n = int(simplified_n.group(2))

    if denominator_x == denominator_n and numerator_x % denominator_x == 0 and numerator_n % denominator_x == 0:
        return True
    return False
