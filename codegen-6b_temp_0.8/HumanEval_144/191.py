
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
    # This is code to check the fraction
    def test(x, n, d):
        return x * n == int(x * n)
    # At this point, we know that the numerator is smaller.
    # If it is a multiple of the denominator, we check the numerator is divisible by the denominator
    # If it is not divisible, we remove the fraction
    if n[0] == '0':
        return False
    elif x[1] == '0' and x[0] == '0':
        return True
    elif n[1] == '0' and n[0] == '0':
        return True
    elif n[0] == '0' and n[1] == '0':
        return True
    elif n[1] == '0' and n[0] != '0':
        return True
    elif x[1] == '0':
        return True
    elif d[1] == '0':
        return True
    elif test(n[0], d[0], d[1]):
        return True
    elif n[0] == d[0]:
        return True
    elif n[1] == d[1]:
        return True
    else:
        return False

