
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
    num_x, denom_x = x.split('/')
    num_n, denom_n = n.split('/')

    denom_prod = int(num_x) * int(denom_n)
    num_prod = int(num_n) * int(denom_x)

    if denom_prod == num_prod:
        return True
    else:
        return False

