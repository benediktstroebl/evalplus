
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

    if not isinstance(x, str) or not isinstance(n, str):
        return False
    if x.count("/")!= 1 or n.count("/")!= 1 or x.count("/")!= 1:
        return False

    num_a = int(x.split("/")[0])
    num_b = int(x.split("/")[1])
    den_a = int(n.split("/")[0])
    den_b = int(n.split("/")[1])
    if den_a == 0 or den_b == 0:
        return False
    if num_a == den_a and num_b == den_b:
        return True
    if num_a == den_a and num_b == den_b * num_a / den_a:
        return True
    elif num_b == den_b and num_a == den_a * num_b / den_b:
        return True

    return False
