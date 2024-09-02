
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
    num = x.split("/")[0]
    den = x.split("/")[1]
    if num == "0" or den == "0":
        return False
    if int(num)!= num or int(den)!= den:
        return False
    if int(num) == 0:
        return False
    if int(den) == 1:
        return True
    if int(num) == int(den):
        return True
    return int(num) * int(den) == int(n)

