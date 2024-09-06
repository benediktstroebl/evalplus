
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
    if x == "0/1":
        return n == "0/1"
    elif n == "0/1":
        return x == "0/1"
    else:
        x_n = x.split("/")[0]
        x_d = x.split("/")[1]
        n_n = n.split("/")[0]
        n_d = n.split("/")[1]
        d = int(x_d) * int(n_d)
        return (int(x_n) * int(n_n) * int(x_d) * int(n_d)) % d == 0

