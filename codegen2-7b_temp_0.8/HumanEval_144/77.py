
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
    if x == n:
        return True
    if x[0] == n[0] and x[1] == n[1]:
        return simplify(x[1] + x[0], n[1] + n[0])
    if n == "0" or x == "0" or x == "0/1":
        return False
    return simplify(x, n[1] + n[0]) or simplify(x[1] + x[0], n)

