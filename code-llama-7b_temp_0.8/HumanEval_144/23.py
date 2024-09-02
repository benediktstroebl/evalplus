
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
    n_num, n_den = n.split("/")
    x_num, x_den = x.split("/")
    gcd_num = gcd(int(x_num), int(n_num))
    gcd_den = gcd(int(x_den), int(n_den))
    if gcd_num == gcd_den == 1:
        return False
    else:
        return (int(x_num) // gcd_num) * int(n_num) * int(x_den) * gcd_den == (
            int(n_num) // gcd_num) * int(x_num) * int(n_den) * gcd_den

