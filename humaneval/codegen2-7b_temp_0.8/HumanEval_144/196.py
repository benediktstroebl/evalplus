
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
    denominator = x.split('/')[1]
    numerator = x.split('/')[0]

    if numerator.isnumeric() and denominator.isnumeric():
        return int(numerator) * int(denominator) == int(x) * int(n)

    if not x.split('/')[0].isnumeric() or not x.split('/')[1].isnumeric():
        return False

