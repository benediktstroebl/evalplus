
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

    x = str(x)
    n = str(n)
    if x[1]!= "/" or n[1]!= "/":
        return False
    if x[0]!= n[0]:
        return False
    numerator, denominator = int(x[:x.index('/')]), int(x[x.index('/') + 1:])
    new_numerator, new_denominator = int(n[:n.index('/')]), int(n[n.index('/') + 1:])
    if numerator * new_denominator == denominator * new_numerator:
        return True
    else:
        return False
