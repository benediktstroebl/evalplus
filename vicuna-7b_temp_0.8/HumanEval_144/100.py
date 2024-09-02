
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
    # check if n is a positive whole number
    if int(n) != n:
        return False
    # convert x and n to integers
    x = int(x)
    n = int(n)
    # multiply x and n
    product = x * n
    # check if product is a whole number
    if product == int(product):
        return True
    else:
        return False
