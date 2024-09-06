
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

    numerator_x, denominator_x = x.split("/")
    numerator_n, denominator_n = n.split("/")
    #print(numerator_x)
    #print(denominator_x)
    #print(numerator_n)
    #print(denominator_n)
    numerator_x = int(numerator_x)
    denominator_x = int(denominator_x)
    numerator_n = int(numerator_n)
    denominator_n = int(denominator_n)
    #print(numerator_x)
    #print(denominator_x)
    #print(numerator_n)
    #print(denominator_n)
    if (numerator_x*denominator_n) == (numerator_n*denominator_x):
        return True
    else:
        return False
