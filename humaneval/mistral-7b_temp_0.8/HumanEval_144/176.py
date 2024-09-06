
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
    x = x.split("/")
    n = n.split("/")

    x[0] = int(x[0])
    x[1] = int(x[1])

    n[0] = int(n[0])
    n[1] = int(n[1])

    return (x[0] * n[1] == x[1] * n[0])
