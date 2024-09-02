
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
    if len(x.split('/'))!= len(n.split('/')):
        return False
    num, den = x.split('/')
    if den == "0":
        return False
    if num == "0":
        return False
    if len(den) > len(num):
        num, den = den, num
    if den[0] == '1':
        return False
    return num == "".join([str(int(num[:i]) * int(num[i:])) for i in range(len(num))]) + "/" + "".join([str(int(den[:i]) * int(den[i:])) for i in range(len(den
