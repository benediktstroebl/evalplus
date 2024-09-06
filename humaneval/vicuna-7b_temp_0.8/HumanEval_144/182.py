
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
    # your code here

    numerator = int(x[0])
    denominator = int(x[1])

    if denominator == 0:
        return False

    numerator_str = str(numerator)
    denominator_str = str(denominator)

    if denominator_str[0] == '1' and denominator_str[1] == '0':
        return False

    if denominator_str[0] == '2' or denominator_str[0] == '3' or denominator_str[0] == '4' or denominator_str[0] == '5':
        return True

    if denominator_str[1] == '1':
        return True

    if denominator_str[1] == '2' or denominator_str[1] == '3' or denominator_str[1] == '4' or denominator_str[1] == '5':
        return True

    if numerator_str[0] == '1' and numerator_str[1] == '0':
        return False

    if numerator_str[0] == '2' or numerator_str[0] == '3' or numerator_str[0] == '4' or numerator_str[0] == '5':
        return True

    if numerator_str[1] == '1':
        return True

    return False