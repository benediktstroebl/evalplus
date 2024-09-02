
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
    if n == "1":
        if x in (y for y in [str(i/10) for i in range(1, 11)] if str(i/10) == x):
            return True
        else:
            return False
    elif n == "2":
        if x in (y for y in [str(i/10) for i in range(2, 11)] if str(i/10) == x):
            return True
        else:
            return False
    elif n == "5":
        if x in (y for y in [str(i/2) for i in range(5, 11)] if str(i/2) == x):
            return True
        else:
            return False
    elif n == "10":
        if x in (y for y in [str(i/10) for i in range(10, 11)] if str(i/10) == x):
            return True
        else:
            return False
    else:
        return False