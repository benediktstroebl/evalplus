
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
    if x.find('/') == -1:
        x = str(int(x) * int(n))
        return x.find('/') == -1
    else:
        x = str(int(x))
        n = str(int(n))
        if x.find('/') == -1 or n.find('/') == -1:
            if x.find('/') == -1 and int(x) * int(n) == int(n):
                return True
            if n.find('/') == -1 and int(x) * int(n) == int(x):
                return True
        else:
            x = int(x)
            n = int(n)
            if (x/n) * (n/x) == int((x/n) * (n/x)):
                return True
            else:
                return False
