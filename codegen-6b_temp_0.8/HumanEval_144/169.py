
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
    if n == '1':
        return True

    if n.index('/') == 0:
        return True

    fractions = n.split('/')
    x = x.split('/')

    # if denominator is 1 return True
    if int(fractions[1]) == 1 and int(x[1]) != 1:
        return True

    # if numerator is 1 return True
    if int(fractions[0]) == 1 and int(x[0]) != 1:
        return True

    # if denominator is 1 return True
    if int(fractions[1]) == 1 and int(x[1]) != 1:
        return True

    # if numerator is 1 return True
    if int(fractions[0]) == 1 and int(x[0]) != 1:
        return True

    # if denominator is 0 return true
    if int(fractions[1]) == 0:
        return True

    # if numerator is 0 return true
    if int(x[0]) == 0:
        return True

    # if numerator is equal to 0 quotient is 0
    if int(fractions[0]) == 0 and int(x[0]) == 0:
        return True

    # if denominator is equal to 0 quotient is 0
    if int(fractions[1]) == 0 and int(x[1]) == 0:
        return True

    fractions[0] = int(fractions[0])
    fractions[1] = int(fractions[1])
    x[0] = int(x[0])
    x[1] = int(x[1])

    # If both denominators are same return True
    if fractions[1] == x[1]:
        return True

    # If both denominators are not same and numerators are same
    if fractions[1] != x[1] and fractions[0] == x[0]:
        return True

    # If both denominators are not same and numerator are not same
    if fractions[1] != x[1] and fractions[0] != x[0]:
        return False

    # Subtract the first fraction from the second fraction
    fractions[0] =