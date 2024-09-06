
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
    # you can use this function to parse x and n
    # function parse(x):
    #     return float(x) / float(n)
    # x = "7/10"
    # n = "10/2"
    # parse(x) = 3.5
    # parse(n) = 5.0
    # simplify(x*n) = True
    # simplify(x*n) = 3.5*5.0 = 17.5
    # simplify(x*n) = False
    # simplify(x*n) = 7.0/2.0 = 3.5
    #
    # to check if n is zero
    if n == "0":
        return False
    # to check if n is zero
    return True