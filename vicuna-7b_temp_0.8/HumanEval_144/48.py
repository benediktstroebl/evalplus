
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
    # check if the numerator and denominator of the strings are the same
    if x[0] != n[0]:
        return False
    # check if the denominator is 1
    if n[1] == "1":
        return simplify_numerator(int(x[0][1:]), int(n[0][1:]))
    else:
        # return False if the numerator is not a whole number
        if x[0][1] != "0" and int(x[0][1:]) != int(n[0][1:]):
            return False
        # simplify the numerator and denominator
        simplified_numerator = simplify_numerator(int(x[0][1:]), int(n[0][1:]))
        simplified_denominator = simplify_denominator(int(x[0][1:]), int(n[0][1:]))
        # check if the simplified numerator and denominator are equal
        if simplified_numerator != simplified_denominator:
            return False
        return True
