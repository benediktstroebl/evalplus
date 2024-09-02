
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
    # convert x and n to tuple form
    # numerator and denominator of x and n
    xn = tuple(map(int, x.split("/")))
    nn = tuple(map(int, n.split("/")))

    # calculate the new numerator and denominator
    new_num = xn[0] * nn[0]
    new_denom = xn[1] * nn[1]

    # if the new numerator is 0 then the fraction will not be simplified
    # otherwise the result is the new numerator divided by new denominator
    return new_num == 0 or new_num % new_denom == 0
