
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

    if x == "0" and n == "0":
        return False
    if x == "0":
        return True
    if n == "0":
        return True
    if "." not in x or "." not in n:
        if x.isdecimal() and n.isdecimal():
            if float(x) * float(n) == int(x) * int(n):
                return True
            else:
                return False
        else:
            return False
    else:
        x = x.split(".")
        n = n.split(".")
        if x[1] == "0" and n[1] == "0":
            if x[0] == "0":
                return True
            else:
                return False
        elif x[0] == "0" and n[0] == "0":
            return True
        else:
            return False
    

