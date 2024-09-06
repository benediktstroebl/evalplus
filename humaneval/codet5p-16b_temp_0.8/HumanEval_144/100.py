
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

    try:
        x, n = x.split('/'), n.split('/')
        x = [int(i) for i in x]
        n = [int(i) for i in n]
        if x[1] == 0:
            raise Exception('Denominator is zero')
        else:
            denominator = x[1] * n[1]
            if denominator < 0:
                denominator = abs(denominator)
                x[1] = denominator
                n[1] = denominator
            if x[0] * n[0] == denominator:
                return True
            else:
                return False
    except:
        return False
