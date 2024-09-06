
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
    x = int(x)
    n = int(n)
    numerator = int(x[0])
    denominator = int(n[0])
    if numerator == 0:
        return False
    if denominator == 0:
        return False
    if denominator != 1:
        if x[1:] == str(denominator) and n[1:] != str(denominator):
            return True
        elif x[1:] == str(denominator) and n[1:] == str(denominator):
            return True
    if denominator != 1:
        if x[1:] == str(denominator) and n[1:] != str(denominator):
            numerator = numerator / denominator
            return simplify(int(x[0])/int(n[0]), int(n[0]))
        elif x[1:] == str(denominator) and n[1:] == str(denominator):
            numerator = numerator / denominator
            return simplify(int(x[0])/int(n[0]), int(n[0]))
    if denominator != 1:
        if n[1:] == str(denominator) and x[1:] != str(denominator):
            numerator = numerator / denominator
            return simplify(int(x[0])/int(n[0]), int(n[0]))
        elif n[1:] == str(denominator) and x[1:] == str(denominator):
            numerator = numerator / denominator
            return simplify(int(x[0])/int(n[0]), int(n[0]))
    return False
