
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
    if x == "0" or n == "0":
        return True
    numerator, denominator = eval(''.join(x).split('/'))
    leading_digit = False
    if '.' in x:
        leading_digit = x[x.index('.')-1] == "0"
    if leading_digit:
        numerator = int(str(numerator) + str(leading_digit))
        denominator = int(str(denominator) + str(leading_digit))
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        return None
    result = str(numerator / denominator)
    if result != int(result) or denominator == 1:
        return False
    return True

