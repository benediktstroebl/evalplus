
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
    numerator_1 = int(x.split('/')[0])
    denominator_1 = int(x.split('/')[1])
    numerator_2 = int(n.split('/')[0])
    denominator_2 = int(n.split('/')[1])

    if (numerator_1 * denominator_2 == numerator_2 * denominator_1) and (denominator_1 != 1 and denominator_2 != 1):
        return True
    elif denominator_1 == 1 or denominator_2 == 1:
        return False
    elif (numerator_1 * denominator_2 == numerator_2 * denominator_1) and (denominator_1 == 1 or denominator_2 == 1):
        return True
    else:
        return False

