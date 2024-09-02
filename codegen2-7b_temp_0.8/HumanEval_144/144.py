
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
    x = x.split("/")
    if x[0] == "0":
        return False

    n = n.split("/")
    if n[0] == "0":
        return False
    if n[1] == "1":
        return True
    if int(x[0]) * int(n[1]) == int(n[0]) * int(x[1]):
        return True
    return False

