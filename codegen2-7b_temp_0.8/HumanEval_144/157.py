
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
    if len(n) == 1:
        if n == '1':
            return True
        elif n == '0':
            return False
        else:
            return False
    else:
        n1 = n.split("/")[0]
        n2 = n.split("/")[1]
        return simplify(x + '/' + n2, n1) or simplify(x + '/' + n2, n2) or simplify(x + '/' + n1, n1) or simplify(x + '/' + n1, n2)
