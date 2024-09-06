
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
    if x == "0" or n == "0":
        return False

    if n.startswith("-"):
        n = n[1:]

    n, x = str(n), str(x)

    if "/" not in n and n.startswith("0"):
        return False

    if "/" in n and "0" in n:
        return False

    before_n, n = n.split("/")
    before_x, x = x.split("/")

    if int(before_x) % int(n) == 0:
        return True

    return False

