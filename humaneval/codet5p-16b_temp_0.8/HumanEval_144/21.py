
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

    if x == "0":
        return False
    elif n == "0":
        return True
    elif "/" in x or "/" in n:
        numerator = x.split("/")[0]
        denominator = x.split("/")[1]
        numerator2 = n.split("/")[0]
        denominator2 = n.split("/")[1]
        if denominator == "0":
            return False
        elif numerator == "0" or denominator2 == "0":
            return True
        elif numerator == "1":
            return True
        elif numerator2 == "1":
            return True
        elif denominator == "1":
            return True
        elif denominator2 == "1":
            return True
        elif numerator == "1/2":
            return True
        elif numerator == "1/4":
            return True
        elif numerator == "1/8":
            return True
        elif numerator == "1/16":
            return
