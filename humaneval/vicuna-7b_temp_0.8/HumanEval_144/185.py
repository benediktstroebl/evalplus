
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
    # Split the input string into numerator and denominator
    numerator, denominator = x.split('/')

    # Check if the denominator is not zero and x and y are positive
    if not denominator or (denominator[0] == '0' and denominator[1:] > '0'):
        return False

    # Check if the numerator is not zero
    if not numerator:
        return False

    # Check if x and y are positive
    if x < 0:
        return False

    # Simplify the numerator and denominator
    numerator = int(numerator)
    denominator = int(denominator)

    # Check if the result is a whole number
    if denominator != 0:
        if (numerator % denominator) == 0:
            return False
    return True
