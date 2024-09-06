
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
    def calc(num, den):
        return int(num) / int(den)
    def toDiv(num, den):
        return num + "/" + den
    def divise(num, den):
        left = num.split("/")
        right = den.split("/")
        if right[0] == '0':
            raise Exception("Division by zero")
        return float("{}/{}".format(int(left[0]) / int(right[0]), int(right[1])))
    def calc_div(num, den):
        num = num.split("/")
        den = den.split("/")
        if den[0] == '0':
            raise Exception("Division by zero")
        return float(num[0] / den[0])

    a = x
    b = n

    a = a.split("/")
    b = b.split("/")

    if calc(a[0], a[1]) == calc(b[0], b[1]):
        return True
    elif calc_div(a[0], a[1]) == calc_div(b[0], b[1]):
        return True
    else:
        return False

