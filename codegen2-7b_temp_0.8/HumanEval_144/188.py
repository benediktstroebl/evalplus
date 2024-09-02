
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
    d = x[::-1].split("/")
    if len(d) == 2:
        d1 = d[0].split("")
        d2 = d[1].split("")

        if d1[0] == "" and d2[0]!= "":
            return True

        for i in range(len(d2)):
            if d2[i] == "0":
                d2[i] = ""

        if d2[0] == "" and d1[0]!= "":
            return True

    return
