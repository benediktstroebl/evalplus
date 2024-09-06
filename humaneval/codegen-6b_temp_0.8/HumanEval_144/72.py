
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
    valid = False
    if x == "0" and n == "1":
        valid = True
    elif x == n:
        valid = True
    elif x != "1" and x != "0" and '/' in x:
        a, b = x.split('/')
        b = n + "/" + b
        valid = simplify(a, b)

    return valid

