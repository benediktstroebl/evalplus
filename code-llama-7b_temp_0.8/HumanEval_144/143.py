
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
    x_num = int(x.split("/")[0])
    x_denom = int(x.split("/")[1])

    n_num = int(n.split("/")[0])
    n_denom = int(n.split("/")[1])

    x_num *= n_denom
    x_denom *= n_num

    # Simplify
    gcd = 0

    for i in range(min(x_denom, x_num), 0, -1):
        if x_num % i == 0 and x_denom % i == 0:
            gcd = i

    if x_num == x_denom == 0:
        return True
    if gcd > 1:
        x_num //= gcd
        x_denom //= gcd

    if x_num % 1 == 0 and x_denom % 1 == 0:
        return True
    else:
        return False

