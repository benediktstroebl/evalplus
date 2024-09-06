
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
    # convert fractions to int
    def fraction_to_int(frac):
        split_frac = frac.split("/")
        return int(split_frac[0])/int(split_frac[1])

    # simple case
    if n == "1/1":
        return True

    # case where n is 1/2
    elif n == "1/2":
        # case where x is even
        if int(x.split("/")[0]) % 2 == 0:
            return True
        # case where x is odd
        else:
            return False

    # case where n is odd
    elif int(n.split("/")[0]) % 2 == 1:
        return int(x) % 2 == 0

    # case where n is even
    else:
        return False
