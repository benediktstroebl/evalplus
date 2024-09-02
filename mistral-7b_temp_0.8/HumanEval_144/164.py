
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

    #your code here

    x1 = x.split('/')
    x1[0] = int(x1[0])
    x1[1] = int(x1[1])

    n1 = n.split('/')
    n1[0] = int(n1[0])
    n1[1] = int(n1[1])

    a = x1[0] * n1[1]
    b = x1[1] * n1[0]
    if a % b == 0:
        return True
    else:
        return False


