
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
    numerator = n.split('/')[0]
    denominator = n.split('/')[1]
    return (x.split('/')[0] + '/' + x.split('/')[1]) == n or (x.split('/')[0] == numerator and x.split('/')[1] == denominator) or (x.split('/')[0] == numerator and x.split('/')[1] == '1') or (x.split('/')[0] == '1' and x.split('/')[1] == denominator) or x.split('/')[0] == numerator or x.split('/')[1] ==
